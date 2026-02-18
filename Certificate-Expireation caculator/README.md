# 📅 Expiration Date Tracker

A simple, robust Python desktop application designed to track item validity, calculate expiration dates, and manage records using a local database. Built with **PySimpleGUI** for the interface and **SQLite** for storage.

## 🚀 Features

* **Automatic Calculation:** Instantly calculates expiration dates and remaining days based on an Issue Date and a custom duration (default: 3 years / 1095 days).
* **Status Tracking:** Automatically determines if an item is "Valid" or "Expired".
* **Database Management:** Stores records (Serial Number, Name, Dates, Status) in a local SQLite database (`records.db`).
* **Data View:** View all saved records in a scrollable window.
* **Excel Export:** Export your entire database to an Excel file (`records.xlsx`) with a single click.
* **User-Friendly Interface:** Clean GUI powered by PySimpleGUI.

## 🛠️ Prerequisites

Ensure you have **Python 3.x** installed on your system. You will also need the following external libraries:

* `PySimpleGUI` (For the Interface)
* `openpyxl` (For Excel Exporting)

*(Note: `sqlite3` and `datetime` are included with Python's standard library.)*

## 📦 Installation

1.  **Clone or Download** this repository.
2.  **Install dependencies** by running the following command in your terminal/command prompt:

    ```bash
    pip install PySimpleGUI openpyxl
    ```

3.  **Run the application**:

    ```bash
    python your_script_name.py
    ```
    *(Replace `your_script_name.py` with the actual name of the python file).*

## 📖 Usage Guide

### 1. Calculate and Save a Record
1.  **Issue Date:** Enter the date in **YYYY-MM-DD** format (e.g., `2023-10-25`).
2.  **Total Days:** Enter the validity duration (Default is `1095` days).
3.  **SN & Name:** Enter the Serial Number and the Name associated with the record.
4.  Click **Calculate** to see the Expiration Date, Days Remaining, and Status.
5.  Click **Save** to store the entry in the database.

### 2. View and Export Records
1.  Click **View Records** on the main dashboard.
2.  A new window will open listing all stored data.
3.  To save this data externally, click the **Export to Excel** button. A file named `records.xlsx` will be created in the application folder.

## 📂 Project Structure

* `main.py`: The core application script.
* `records.db`: The SQLite database file (automatically created upon first run).
* `records.xlsx`: The exported Excel file (created upon export).

## ⚠️ Known Limitations / To-Do
* **Manage Employees:** The button is currently a placeholder for future functionality.
* **Date Format:** The application currently strictly requires `YYYY-MM-DD`. Entering other formats may cause an error.

## 🤝 Contributing

Feel free to fork this project and submit pull requests. You can also open issues if you find bugs or want to suggest features (like implementing the Delete function or the Manage Employees module).

## 📄 License

This project is open-source and available for personal and educational use.
