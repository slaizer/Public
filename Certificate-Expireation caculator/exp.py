import PySimpleGUI as sg
from datetime import datetime, timedelta
import sqlite3
from openpyxl import Workbook

# Functions for expiration calculations
def calculate_expiration(issue_date: datetime, days=1095) -> datetime:
    return issue_date + timedelta(days=days)

def days_remaining(expiration_date: datetime) -> int:
    today = datetime.today()
    return (expiration_date - today).days

def status(expiration_date: datetime) -> str:
    today = datetime.today()
    return 'Valid' if today <= expiration_date else 'Expired'

# SQLite Functions
def init_db():
    with sqlite3.connect('records.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS records
        (sn TEXT, name TEXT, issue_date TEXT, expiration_date TEXT, status TEXT)
        ''')

def save_to_db(sn, name, issue_date, expiration_date, status):
    with sqlite3.connect('records.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO records (sn, name, issue_date, expiration_date, status) VALUES (?, ?, ?, ?, ?)",
                       (sn, name, issue_date, expiration_date, status))
        conn.commit()

def fetch_records():
    with sqlite3.connect('records.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT sn, name, issue_date, expiration_date, status, \
                       julianday(expiration_date) - julianday('now') as remaining_days FROM records")
        return cursor.fetchall()

def delete_record(sn):
    with sqlite3.connect('records.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM records WHERE sn = ?", (sn,))
        conn.commit()

def export_to_excel(records):
    wb = Workbook()
    ws = wb.active
    ws.append(['SN', 'Name', 'Issue Date', 'Expiration Date', 'Status', 'Remaining Days'])
    for record in records:
        ws.append(record)
    filename = 'records.xlsx'
    wb.save(filename)
    return filename

# Initialize the database (create the table if it doesn't exist)
init_db()

# Main GUI Layout
layout = [
    [sg.Text('Issue Date (YYYY-MM-DD):'), sg.InputText(key='ISSUE_DATE')],
    [sg.Text('Total Days (Default 1095):'), sg.InputText(default_text='1095', key='TOTAL_DAYS')],
    [sg.Text('SN:'), sg.InputText(key='SN')],
    [sg.Text('Name:'), sg.InputText(key='NAME')],
    [sg.Button('Calculate'), sg.Button('Save'), sg.Button('View Records'), sg.Button('Manage Employees'), sg.Button('Exit')],
    [sg.Text('Expiration Date:'), sg.Text('', size=(25,1), key='EXPIRATION')],
    [sg.Text('Days Remaining:'), sg.Text('', size=(25,1), key='DAYS_REMAINING')],
    [sg.Text('Status:'), sg.Text('', size=(25,1), key='STATUS')]
]

window = sg.Window('Expiration Calculator', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Calculate':
        try:
            issue_date = datetime.strptime(values['ISSUE_DATE'], '%Y-%m-%d')
            total_days = int(values['TOTAL_DAYS'])
            expiration_date = calculate_expiration(issue_date, total_days)
            window['EXPIRATION'].update(expiration_date.strftime('%Y-%m-%d'))
            window['DAYS_REMAINING'].update(days_remaining(expiration_date))
            window['STATUS'].update(status(expiration_date))
        except Exception as e:
            sg.PopupError(f"An error occurred: {e}")

    if event == 'Save':
        try:
            save_to_db(values['SN'], values['NAME'], values['ISSUE_DATE'], window['EXPIRATION'].get(), window['STATUS'].get())
            sg.Popup('Record saved successfully!')
        except Exception as e:
            sg.PopupError(f"Error saving to database: {e}")

    if event == 'View Records':
        records = fetch_records()
        if not records:
            sg.Popup('No records found in the database!')
            continue
        record_layout = [
            [sg.Text('SN', size=(10, 1)), sg.Text('Name', size=(20, 1)), sg.Text('Issue Date', size=(15, 1)),
             sg.Text('Expiration Date', size=(15, 1)), sg.Text('Status', size=(10, 1)),
             sg.Text('Remaining Days', size=(15, 1)),
             sg.Button('Export to Excel')]
        ]
        for record in records:
            record_layout.append([
                sg.Text(record[0], size=(10, 1)),
                sg.Text(record[1], size=(20, 1)),
                sg.Text(record[2], size=(15, 1)),
                sg.Text(record[3], size=(15, 1)),
                sg.Text(record[4], size=(10, 1)),
                sg.Text(str(int(record[5])) if record[5] else 'N/A', size=(15, 1))
            ])

        screen_width, screen_height = sg.Window.get_screen_size()
        column_width = int(screen_width * 0.8)
        column_height = int(screen_height * 0.8)
        scrollable_column = sg.Column(record_layout, scrollable=True, vertical_scroll_only=False,
                                      size=(column_width, column_height))

        record_layout = [[scrollable_column], [sg.Button('Close')]]
        record_window = sg.Window('Records from Database', record_layout, resizable=True, finalize=True,
                                  return_keyboard_events=True)
        record_window.Maximize()

        while True:
            re_event, re_values = record_window.read()
            if re_event in (sg.WIN_CLOSED, 'Close'):
                record_window.close()
                break
            if re_event == 'Export to Excel':
                try:
                    filename = export_to_excel(records)
                    sg.Popup(f'Records exported successfully to {filename}!')
                except Exception as e:
                    sg.PopupError(f"Error exporting to Excel: {e}")

    # Add logic for 'Manage Employees' when the requirement is clear

window.close()
