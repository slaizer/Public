import subprocess
import sqlite3
import PySimpleGUI as sg
import winsound
import threading
import time
import re
from collections import defaultdict
from datetime import datetime

# History dictionary
history = defaultdict(list)

def get_ping_status(ip):
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        result = subprocess.run(['ping', '-n', '1', '-w', '1000', ip], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, startupinfo=startupinfo)
        output = result.stdout.decode()
        if "Destination host unreachable" in output:
            return 'down', None
        else:
            match = re.search('Average = (\d+)ms', output)
            if match:
                delay = float(match.group(1))
                return 'up', delay
            else:
                return 'down', None
    except Exception as e:
        return 'down', None
    return 'unknown', None

conn = sqlite3.connect('ip_database.db')
c = conn.cursor()
c.execute('SELECT name, ip_address FROM ips_table')
ip_data = c.fetchall()
conn.close()

layout = []
for name, ip in ip_data:
    layout.append([sg.Text(f'Ping Status {name} ({ip}):'), sg.Text(size=(15,1), key=f'-OUTPUT-{ip}-', text_color='white', background_color='black'), sg.Text('Latency:'), sg.Text(size=(10,1), key=f'-LATENCY-{ip}-'), sg.Button('History', key=f'-HISTORY-{ip}-')])

window = sg.Window('Ping Status', layout, finalize=True, resizable=True)

def ping_and_update(ip, name, window):
    while True:
        status, delay = get_ping_status(ip)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if status == 'up':
            window.write_event_value('-UPDATE-', (ip, 'up', delay))
            history[ip].append((timestamp, delay))
        else:
            window.write_event_value('-UPDATE-', (ip, 'down', None))
            winsound.Beep(frequency=2500, duration=1000)
            history[ip].append((timestamp, None))
        time.sleep(5)

for name, ip in ip_data:
    threading.Thread(target=ping_and_update, args=(ip, name, window), daemon=True).start()
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif '-UPDATE-' in event:
        ip, status, delay = values['-UPDATE-']
        if status == 'up':
            window[f'-OUTPUT-{ip}-'].update(status, text_color='black', background_color='green')
            window[f'-LATENCY-{ip}-'].update(f'{delay} ms')
        else:
            window[f'-OUTPUT-{ip}-'].update(status, text_color='white', background_color='red')
            window[f'-LATENCY-{ip}-'].update('N/A')
    elif '-HISTORY-' in event:
        ip = event.split('-')[-2] # Extract the IP from the event string
        history_window_layout = [[sg.Listbox(values=[f'{x[0]}: {x[1] if x[1] is not None else "N/A"} ms' for x in reversed(history[ip])], size=(60, 20))]]
        history_window = sg.Window(f'Ping history for {ip}', history_window_layout, modal=True)
        history_window.read(close=True)

window.close()
sg.Popup("Thanks for using IP Monitor//Sudo-Gate \U0001F47B ")
