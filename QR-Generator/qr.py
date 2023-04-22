
import PySimpleGUI as sg
import os
import  qrcode
layout = [
    [sg.Text("Enter Google Maps link:"), sg.InputText(key="link")],
    [sg.Button("Generate QR code"), sg.Button("Open QRCODE")],
]

window = sg.Window("NAS-WATANIA QR ", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Generate QR code":
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(values["link"])
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        img.save("QR.png")
    elif event == "Open QRCODE":
        file_path = r"QR.png"
        os.startfile(file_path)

window.close()
