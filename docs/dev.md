# **Developer's Guide**

## **GridCode Asset Management System**

The Asset Management System is a Python program designed to manage information about assets in a CSV file. This document provides an overview of the code structure, its functionalities, and how to use the system.

## **Table of Contents**

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Code Structure](#code-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [Suggesting Enhancements](#suggesting-enhancements)
- [License](#license)

## **Introduction**

The Asset Management System is implemented in Python and utilizes CSV files for storing asset information. The system allows users to create, read, update, and delete assets, providing a simple interface for managing asset data.

## **Getting Started**

To use the Asset Management System, follow these steps:

### **Clone the Repository:**
```bash
git clone https://github.com/amarquaye/gridcode.git
cd gridcode
```

### **Run the program:**
```python
python main.py
```

### **Code Structure:**
```python
The code is organized into a class-based structure with the following components:

***Class: AssetManagementSystem*** 
__init__(self): Initializes the system by checking if the 'assets.csv' file exists and defining fieldnames.

get_last_asset_id(self): Helper function to retrieve the ID of the last asset in the CSV file.

create_asset(self): Allows users to create a new asset, generating a unique ID and writing the asset details to the CSV file.

read_assets(self): Displays a list of all assets stored in the CSV file.

update_asset(self): Allows users to update the details of a specific asset.

delete_asset(self): Allows users to delete a specific asset.

```


### **Code Breakdown**
#### **1. Initialization**
```python
import csv
import os
import sys

class AssetManagementSystem:
    def __init__(self):
        # Check if the file exists
        self.file_exists = os.path.isfile('assets.csv')

        # Open the CSV file in append mode
        self.fieldnames = ['ID', 'SN', 'CATEGORY', 'TYPE', 'LOCATION', 'DESCRIPTION', 'COLOR', 'STATUS']
        self.header_printed = False  # Flag to track whether the header has been printed

```
##### **Explanation:**
This section is part of a class called AssetManagementSystem.
os.path.isfile('assets.csv') checks whether a file named 'assets.csv' exists. This is crucial because the program needs to interact with this file for managing assets.
self.fieldnames defines the column headers for the CSV file, representing various attributes of each asset.
self.header_printed is a flag used to track whether the header has been printed when writing to the CSV file.

#### **2. Get Last Asset ID**
```python
def get_last_asset_id(self):
        try:
            with open('assets.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)
                if rows:
                    return int(rows[-1]['ID'])
                else:
                    return 0
        except FileNotFoundError:
            return 0
```
##### **Explanation:**
This method aims to retrieve the last used asset ID from the CSV file.
It uses a try block to handle potential file-not-found errors (FileNotFoundError).
It opens the 'assets.csv' file in read mode and uses csv.DictReader to read the CSV data into a list of dictionaries (rows).
If there are rows (assets) in the file, it returns the ID of the last asset; otherwise, it returns 0.
If the file is not found, it also returns 0.

#### **3. Create Asset**
```python
def create_asset(self):
        # ... (input prompts)
        with open('assets.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)

            # Write header only if it hasn't been printed yet
            if not self.header_printed:
                writer.writeheader()
                self.header_printed = True

            # Write the new asset
            writer.writerow({'ID': ID, 'SN': sn, 'CATEGORY': asset_category, 'TYPE': asset_type,
                             'LOCATION': location, 'DESCRIPTION': description, 'COLOR': color, 'STATUS': status})
        print(f"Asset '{sn}' added successfully!\n")
```
##### **Explanation:**
This method allows the user to input details for a new asset.
It uses a with statement to open the 'assets.csv' file in append mode.
csv.DictWriter is employed to write data to the CSV file using dictionaries.
It checks whether the header has been printed. If not, it prints the header.
It then writes a new row (asset) to the CSV file with details provided by the user.
Finally, it prints a success message.

#### **4. Read Assets**
```python
def read_assets(self):
        try:
            with open('assets.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                # ... (printing asset details)
        except FileNotFoundError:
            print("No assets found.\n")
```
##### **Explanation:**
This method reads and displays existing assets from 'assets.csv'.
It uses a try block to handle potential file-not-found errors (FileNotFoundError).
It opens the 'assets.csv' file in read mode using csv.DictReader.
It then iterates through each row and prints details of each asset.

#### **5. Update Asset**
```python
def update_asset(self):
        # ... (input prompts)
        rows = []
        updated = False
        try:
            with open('assets.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                # ... (updating specified asset field)
        except FileNotFoundError:
            print("No assets found.\n")
``` 
##### **Explanation:**
This method updates the specified field of a chosen asset.
It uses a try block to handle potential file-not-found errors (FileNotFoundError).
It reads the 'assets.csv' file, iterates through each row, and updates the specified field of the chosen asset.
If the asset is found and updated, it writes the changes back to the file.
If the asset is not found, it prints a message indicating so.

#### **6. Delete Asset**
```python
def delete_asset(self):
        # ... (input prompt)
        rows = []
        deleted = False
        try:
            with open('assets.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                # ... (deleting specified asset)
        except FileNotFoundError:
            print("No assets found.\n")
```
##### **Explanation:**
This method deletes a specified asset based on its serial number.
It uses a try block to handle potential file-not-found errors (FileNotFoundError).
It reads the 'assets.csv' file, identifies the asset to delete, and writes the changes back to the file.
If the asset is not found, it prints a message indicating so.

#### **7. Main Function**
```python
def main():
    asset_system = AssetManagementSystem()
    # ... (menu and user interaction)
if __name__ == "__main__":
    main()
```
##### **Explanation:**
The main function is the entry point of the program.
It creates an instance of the AssetManagementSystem class.
It then runs a loop for user interaction, presenting a menu for creating, reading, updating, or deleting assets.
It allows the user to exit the system by entering '5'.

## **Usage**
Run the program by executing ```python main.py```

Choose from the following options:

Create Asset (1): Enter details for a new asset.<br>
Read Assets (2): View a list of all assets.<br>
Update Asset (3): Modify details of an existing asset.<br>
Delete Asset (4): Remove a specific asset.<br>
Exit (5): Terminate the program.

## **Contributing**
Contributions to the Asset Management System are welcome. Please follow the guidelines outlined below.
- Fork the repository on GitHub.
- Clone your forked repository to your local machine.
- Make changes in your local repository.
- Push your changes to your fork on GitHub.
- Submit a pull request.

### **Suggesting Enhancements**
To suggest an enhancement, create a GitHub Issue with the following information:

- A clear and descriptive title.
- A detailed description of the enhancement.
- If possible, provide examples or use cases.

### **Code Review Process**
- All contributions will be reviewed by a maintainer.
- Feedback will be provided, and necessary changes may be requested.

## **License**
By contributing to the Asset Management System, you agree that your contributions will be licensed under the [Apache 2.0](https://github.com/amarquaye/gridcode/blob/master/LICENSE).
