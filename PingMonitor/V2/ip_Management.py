import sqlite3
import PySimpleGUI as sg

def fetch_ips():
    # Connect to the SQLite database and fetch all data
    conn = sqlite3.connect('ip_database.db')
    c = conn.cursor()
    c.execute('SELECT name, ip_address FROM ips_table')
    data = c.fetchall()
    conn.close()
    return data

# Layout for the window
layout = [
    [sg.Text('Name'), sg.Input(key='-NAME-')],
    [sg.Text('IP Address'), sg.Input(key='-IP-')],
    [sg.Button('Submit'), sg.Button('Show All'), sg.Button('Remove Selected'), sg.Button('Exit')],
    [sg.Listbox(values=[], size=(60, 10), key='-LISTBOX-')]
]

# Create the window
window = sg.Window('Manage IP Addresses', layout)

while True:
    event, values = window.read()
    # End program if user closes window or presses the Exit button
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        name = values['-NAME-']
        ip = values['-IP-']
        # Connect to the SQLite database and insert the data
        conn = sqlite3.connect('ip_database.db')
        c = conn.cursor()
        c.execute('INSERT INTO ips_table VALUES (?, ?)', (name, ip))
        conn.commit()
        conn.close()
        sg.popup('Data inserted successfully!')
    if event == 'Show All':
        data = fetch_ips()
        window['-LISTBOX-'].update(data)
    if event == 'Remove Selected':
        selected = values['-LISTBOX-'][0]
        name, ip = selected[0], selected[1]
        # Connect to the SQLite database and remove the selected data
        conn = sqlite3.connect('ip_database.db')
        c = conn.cursor()
        c.execute('DELETE FROM ips_table WHERE name = ? AND ip_address = ?', (name, ip))
        conn.commit()
        conn.close()
        sg.popup('Data removed successfully!')

window.close()
