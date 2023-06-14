import subprocess
import sqlite3
import PySimpleGUI as sg
import winsound
import threading
import time
import re

def get_ping_status(ip):
    try:
        # Run the ping command
        result = subprocess.run(['ping', '-n', '1', '-w', '1000', ip], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # Check the output
        output = result.stdout.decode()
        if "Destination host unreachable" in output:
            return 'down', None
        else:
            # Extract the time from the output
            match = re.search('Average = (\d+)ms', output)
            if match:
                delay = float(match.group(1))
                return 'up', delay
            else:
                return 'down', None
    except Exception as e:
        return 'down', None

    # Added this line to handle unexpected output
    return 'unknown', None

conn = sqlite3.connect('ip_database.db')
c = conn.cursor()
c.execute('SELECT name, ip_address FROM ips_table')
ip_data = c.fetchall()
conn.close()

layout = [[sg.Text(f'Ping Status {name} ({ip}):'), sg.Text(size=(15,1), key=f'-OUTPUT-{ip}-', text_color='white', background_color='black'), sg.Text('Latency:'), sg.Text(size=(10,1), key=f'-LATENCY-{ip}-')] for name, ip in ip_data]

window = sg.Window('Ping Status', layout, finalize=True)

def ping_and_update(ip, name, window):
    while True:
        status, delay = get_ping_status(ip)
        if status == 'up':
            window.write_event_value('-UPDATE-', (ip, 'up', delay))
        else:  # This now handles 'down', 'packet_loss', and 'unknown'
            window.write_event_value('-UPDATE-', (ip, 'down', None))
            winsound.Beep(frequency=2500, duration=1000)
        time.sleep(5)

for name, ip in ip_data:
    threading.Thread(target=ping_and_update, args=(ip, name, window), daemon=True).start()

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-UPDATE-':
        ip, status, delay = values['-UPDATE-']
        if status == 'up':
            window[f'-OUTPUT-{ip}-'].update(status, text_color='black', background_color='green')
            window[f'-LATENCY-{ip}-'].update(f'{delay} ms')
        else:
            window[f'-OUTPUT-{ip}-'].update(status, text_color='white', background_color='red')
            window[f'-LATENCY-{ip}-'].update('N/A')

window.close()
