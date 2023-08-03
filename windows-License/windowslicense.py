import winreg
import PySimpleGUI as sg

def get_windows_product_key():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        value, _ = winreg.QueryValueEx(key, "DigitalProductId")
        key.Close()

        product_key = decode_product_key(list(value))
        return product_key
    except Exception as e:
        print(f"Error: {e}")
        return None

def decode_product_key(encoded_key):
    const_table = "BCDFGHJKMPQRTVWXY2346789"
    product_key = ""

    for i in range(25, -1, -1):
        key_index = 0
        for j in range(14, -1, -1):
            key_index = (key_index << 8) + encoded_key[j]
            encoded_key[j] = key_index // 24
            key_index = key_index % 24
        product_key = const_table[key_index] + product_key
        if i % 5 == 0 and i != 0:
            product_key = "-" + product_key

    return product_key

# Create the GUI layout
layout = [
    [sg.Text("Click the button to retrieve the Windows License Key.")],
    [sg.Button("Retrieve License Key"), sg.Button("Exit")],
    [sg.Output(size=(50, 5), key="-OUTPUT-")]
]

# Create the window
window = sg.Window("Windows License Key Extractor", layout)

# Event loop
while True:
    event, _ = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Exit":
        confirm = sg.popup_ok_cancel("Are you sure you want to exit?", title="Confirmation")
        if confirm == "OK":
            print("Exiting the application...")
            break
    elif event == "Retrieve License Key":
        license_key = get_windows_product_key()
        if license_key:
            window["-OUTPUT-"].print(f"Windows License Key: {license_key}")
        else:
            window["-OUTPUT-"].print("Failed to retrieve the Windows License Key.")

# Close the window
window.close()
