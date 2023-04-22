import firebase_admin
from firebase_admin import credentials, firestore
import PySimpleGUI as sg

cred = credentials.Certificate('ServicekeyFile.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

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

window = sg.Window('Dnoitify MAP Set', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Update1':
        doc_ref = db.collection('google-map').document('Maps')
        doc_ref.update({
            'map1': values['map1']
        })
        sg.popup('Map1 updated successfully')
    elif event == 'Update2':
        doc_ref = db.collection('google-map').document('Maps')
        doc_ref.update({
            'map2': values['map2']
        })
        sg.popup('Map2 updated successfully')
    elif event == 'Update3':
        doc_ref = db.collection('google-map').document('Maps')
        doc_ref.update({
            'map3': values['map3']
        })
        sg.popup('Map3 updated successfully')
    elif event == 'Update4':
        doc_ref = db.collection('google-map').document('Maps')
        doc_ref.update({
            'map4': values['map4']
        })
        sg.popup('Map4 updated successfully')
    elif event == 'Update5':
        doc_ref = db.collection('google-map').document('Maps')
        doc_ref.update({
            'map5': values['map5']
        })
        sg.popup('Map5 updated successfully')
    elif event == 'Update6':
        doc_ref = db.collection('google-map').document('Maps')
        doc_ref.update({
            'map6': values['map6']
        })
        sg.popup('Map6 updated successfully')
    elif event == 'Update7':
        doc_ref = db.collection('google-map').document('Maps')
        doc_ref.update({
            'map7': values['map7']
        })
        sg.popup('Map7 updated successfully')
    elif event == 'Update8':
        doc_ref = db.collection('google-map').document('Maps')
        doc_ref.update({
            'map8': values['map8']
        })
        sg.popup('Map8 updated successfully')

window.close()