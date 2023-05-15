import sqlite3
import PySimpleGUI as sg

# Connect to the database and create a cursor
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Define the layout for the GUI
layout = [
    [sg.Text('Item Name:'), sg.InputText(key='item')],
    [sg.Text('Quantity:'), sg.InputText(key='quantity')],
    [sg.Text('Price:'), sg.InputText(key='price')],
    [sg.Text('Project:'), sg.InputText(key='project')],
    [sg.Button('Submit'), sg.Button('Show Purchases'), sg.Button('Remove')],
    [sg.Table(values=[], headings=['Item Name', 'Quantity', 'Price', 'Total Price', 'Project'], key='output', enable_events=True, justification='left', auto_size_columns=True)]
]

# Create the window
window = sg.Window('Purchase Entry', layout)

# Event loop to process GUI events
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Submit':
        # Retrieve input values
        item = values['item']
        quantity = int(values['quantity'])
        price = float(values['price'])
        total_price = quantity * price
        project = values['project']

        # Insert values into the Purchase table
        insert_query = "INSERT INTO Purchase (item_Name, quantity, Price, Total_Price, Project) VALUES (?, ?, ?, ?, ?)"
        insert_values = (item, quantity, price, total_price, project)
        cursor.execute(insert_query, insert_values)

        # Commit the changes
        conn.commit()

        # Display a message box to confirm the insertion
        sg.popup(f"Item '{item}' added to the database.")

    if event == 'Show Purchases':
        # Retrieve all rows from the Purchase table
        select_query = "SELECT item_Name, quantity, Price, Total_Price, Project FROM Purchase"
        cursor.execute(select_query)
        rows = cursor.fetchall()

        # Update the table element with the output rows
        window['output'].update(values=rows)

    if event == 'Remove':
        # Retrieve input value to remove
        item = values['item']

        # Delete the specified item from the Purchase table
        delete_query = "DELETE FROM Purchase WHERE item_Name = ?"
        delete_values = (item,)
        cursor.execute(delete_query, delete_values)

        # Commit the changes
        conn.commit()

        # Display a message box to confirm the removal
        sg.popup(f"Item '{item}' removed from the database.")

# Close the database connection and the window
conn.close()
window.close()
