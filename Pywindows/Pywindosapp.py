import PySimpleGUI as sg
import winreg
import subprocess
import os

def change_pc_name(new_name):
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                         r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters", 0,
                         winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, "Hostname", 0, winreg.REG_SZ, new_name)
    winreg.SetValueEx(key, "NV Hostname", 0, winreg.REG_SZ, new_name)
    winreg.CloseKey(key)
    os.system("shutdown /r /t 0")

def clear_firefox_cache():
    firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    command = f'"{firefox_path}" -P "default" -silent -nosplash -clearCache'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = p.communicate()
    if error:
        print(f"An error occurred: {error.decode('utf-8')}")
    else:
        print("Cache cleared successfully.")

def clear_chrome_cache():
    command = 'start chrome --disk-cache-dir="C:\chrome_cache\data"'
    command2 = 'taskkill /f /im chrome.exe'
    p = subprocess.Popen(["cmd", "/c", command2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen(["cmd", "/c", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    print(output.decode("utf-8"))

def clear_edge_cache():
    command = 'start msedge --disk-cache-dir="C:\msedge_cache\data"'
    command2 = 'taskkill /f /im msedge.exe'
    p = subprocess.Popen(["cmd", "/c", command2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen(["cmd", "/c", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    print(output.decode("utf-8"))

def ip_release():
    subprocess.call("ipconfig /release")

def ip_renew():
    subprocess.call("ipconfig /renew")

def flush_dns():
    subprocess.call("ipconfig /flushdns")

def check_dns(domain):
    subprocess.call(["nslookup", domain])

layout = [
    [sg.Button('Change PC Name'), sg.Input(key='-NEW_NAME-')],
    [sg.Button('Clear Firefox Cache')],
    [sg.Button('Clear Chrome Cache')],
    [sg.Button('Clear Edge Cache')],
    [sg.Button('IP Release')],
    [sg.Button('IP Renew')],
    [sg.Button('Flush DNS')],
    [sg.Button('Check DNS'), sg.Input(key='-DOMAIN-')],
    [sg.Output(size=(50,10))],
]

window = sg.Window('My custom window', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Change PC Name':
        change_pc_name(values['-NEW_NAME-'])
    elif event == 'Clear Firefox Cache':
        clear_firefox_cache()
    elif event == 'Clear Chrome Cache':
        clear_chrome_cache()
    elif event == 'Clear Edge Cache':
        clear_edge_cache()
    elif event == 'IP Release':
        ip_release()
    elif event == 'IP Renew':
        ip_renew()
    elif event == 'Flush DNS':
        flush_dns()
    elif event == 'Check DNS':
        check_dns(values['-DOMAIN-'])

window.close()
