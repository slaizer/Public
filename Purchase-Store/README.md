<div align="center">

  <h1>🛒 Project Purchase Tracker</h1>
  
  <p>
    <b>A lightweight GUI application for managing project expenses.</b><br>
    Built with Python, PySimpleGUI, and SQLite.
  </p>

  <p>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python" alt="Python" />
    </a>
    <a href="https://pysimplegui.readthedocs.io/">
      <img src="https://img.shields.io/badge/GUI-PySimpleGUI-green?style=flat" alt="PySimpleGUI" />
    </a>
    <a href="https://www.sqlite.org/index.html">
      <img src="https://img.shields.io/badge/Database-SQLite3-003B57?style=flat&logo=sqlite" alt="SQLite" />
    </a>
  </p>

</div>

---

## 📝 Overview

This application provides a simple interface for tracking items purchased for specific projects. It automatically calculates total costs and stores all data in a local SQLite database.

## ✨ Features

* **➕ Add Purchases:** Input item details (Name, Quantity, Price, Project).
* **💰 Auto-Calculation:** Automatically calculates `Total Price` (Quantity × Price).
* **👀 View History:** "Show Purchases" button displays a table of all recorded entries.
* **❌ Remove Items:** Delete entries from the database by Item Name.
* **💾 Persistent Storage:** Data is saved to `database.db`.

---

## 🛠️ Installation & Requirements

### 1. Prerequisites
Ensure you have Python installed. You will also need to install the GUI library:

```bash
pip install PySimpleGUI
```


🚀 How to Use
Run the Application:

```bash
python your_script_name.py
```

Add an Item: Fill in the fields (Name, Quantity, Price, Project) and click Submit.

View Data: Click Show Purchases to see the table update with your data.

Delete an Item: Type the name of the item you want to delete in the "Item Name" box and click Remove.

📂 Project Structure
main.py: The application script (GUI and logic).

database.db: The SQLite database file (stores your data).

⚠️ Limitations
Deletion Logic: The "Remove" button deletes items based on the Item Name. If multiple items have the same name, the current logic may delete all of them.

Input Validation: Ensure you enter numbers for "Quantity" and "Price" to avoid errors.

🤝 Contributing
Pull requests are welcome! Ideal future improvements:

[ ] Add an ID column for safer deletion.

[ ] Add an "Export to CSV" feature.

[ ] Add input validation (prevent crashes if text is entered in price fields).

📄 License
Open source and free to use.



