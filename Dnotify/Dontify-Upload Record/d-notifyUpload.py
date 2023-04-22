import firebase_admin
from firebase_admin import credentials, firestore
import PySimpleGUI as sg

# Initialize Firebase Admin SDK
cred = credentials.Certificate('projetexe-db2ce-firebase-adminsdk-u8dj2-26cab882ef.json')
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()

# Define the layout for the PySimpleGUI window
layout = [
    [sg.Text('Update map1')],
    [sg.Input(key='map1')],
    [sg.Button('Update1')],
    [sg.Text('Update map2')],
    [sg.Input(key='map2')],
    [sg.Button('Update2')],
    [sg.Text('Update map3')],
    [sg.Input(key='map3')],
    [sg.Button('Update3')],
    [sg.Text('Update map4')],
    [sg.Input(key='map4')],
    [sg.Button('Update4')],
    [sg.Text('Update map5')],
    [sg.Input(key='map5')],
    [sg.Button('Update5')],
    [sg.Text('Update map6')],
    [sg.Input(key='map6')],
    [sg.Button('Update6')],
    [sg.Text('Update map7')],
    [sg.Input(key='map7')],
    [sg.Button('Update7')],
    [sg.Text('Update map8')],
    [sg.Input(key='map8')],
    [sg.Button('Update8')]

]

# Create the PySimpleGUI window
window = sg.Window('NAS-WATANIA Delivery MAP Set', layout)

# Event loop to process PySimpleGUI events
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Update1':
        # Get a reference to the 'Maps' document in the 'google-map' collection
        doc_ref = db.collection('google-map').document('Maps')
        # Update the document with the value entered by the user
        doc_ref.update({
            'map1': values['map1']
        })
        # Display a message to confirm the update
        sg.popup('Map1 updated successfully')
    elif event == 'Update2':
        # Get a reference to the 'Maps' document in the 'google-map' collection
        doc_ref = db.collection('google-map').document('Maps')
        # Update the document with the value entered by the user
        doc_ref.update({
            'map2': values['map2']
        })
        # Display a message to confirm the update
        sg.popup('Map2 updated successfully')
    elif event == 'Update3':
        # Get a reference to the 'Maps' document in the 'google-map' collection
        doc_ref = db.collection('google-map').document('Maps')
        # Update the document with the value entered by the user
        doc_ref.update({
            'map3': values['map3']
        })
        # Display a message to confirm the update
        sg.popup('Map3 updated successfully')
    elif event == 'Update4':
        # Get a reference to the 'Maps' document in the 'google-map' collection
        doc_ref = db.collection('google-map').document('Maps')
        # Update the document with the value entered by the user
        doc_ref.update({
            'map4': values['map4']
        })
        # Display a message to confirm the update
        sg.popup('Map4 updated successfully')
    elif event == 'Update5':
        # Get a reference to the 'Maps' document in the 'google-map' collection
        doc_ref = db.collection('google-map').document('Maps')
        # Update the document with the value entered by the user
        doc_ref.update({
            'map5': values['map5']
        })
        # Display a message to confirm the update
        sg.popup('Map5 updated successfully')
    elif event == 'Update6':
        # Get a reference to the 'Maps' document in the 'google-map' collection
        doc_ref = db.collection('google-map').document('Maps')
        # Update the document with the value entered by the user
        doc_ref.update({
            'map6': values['map6']
        })
        # Display a message to confirm the update
        sg.popup('Map6 updated successfully')
    elif event == 'Update7':
        # Get a reference to the 'Maps' document in the 'google-map' collection
        doc_ref = db.collection('google-map').document('Maps')
        # Update the document with the value entered by the user
        doc_ref.update({
            'map7': values['map7']
        })
        # Display a message to confirm the update
        sg.popup('Map7 updated successfully')
    elif event == 'Update8':
        # Get a reference to the 'Maps' document in the 'google-map' collection
        doc_ref = db.collection('google-map').document('Maps')
        # Update the document with the value entered by the user
        doc_ref.update({
            'map8': values['map8']
        })
        # Display a message to confirm the update
        sg.popup('Map8 updated successfully')

# Close the PySimpleGUI window
window.close()