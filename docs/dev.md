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

#### Asset Management System Class (AssetManagementSystem):

#### Initialization:

```py
def __init__(self):
    self.file_exists = os.path.isfile('assets.csv')
    self.ID = 'ID'
    self.SN = 'SN'
    # ... (other column headers)
    self.STATUS = 'STATUS'
    logging.basicConfig(filename='assets.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s',
                        datefmt='%A, %Y-%m-%d %I:%M:%S %p')

```

##### **Explanation**:

Initializes the AssetManagementSystem.
Checks if the 'assets.csv' file exists.
Defines column headers for the CSV file.
Configures logging to log activities to 'assets.log'.

#### log_activity Method:

```py
def log_activity(self, message):
    logging.info(message)

```

##### **Explanation:**

Logs an activity message using the logging module.

#### get_last_asset_id Method:

```py
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

Reads the 'assets.csv' file to get the last asset ID.
Returns 0 if the file doesn't exist.

#### create_asset Method:

```py
def create_asset(self):
    # ... (prompting user for asset details)
    try:
        with open('assets.csv', 'a', newline='') as csvfile:
            # ... (writing the new asset to the CSV file)
        print(f"Asset '{sn}' added successfully!\n")
    except PermissionError:
        print("Cannot access file\nPlease close your spreadsheet reader and try again!")

```

##### **Explanation:**

Prompts the user for asset details.
Checks for serial number uniqueness.
Appends the new asset to 'assets.csv'.
Logs the activity.
Handles PermissionError if the file is open in another application.

#### is_serial_number_unique Method:

```py
def is_serial_number_unique(self, serial_number):
    with open('assets.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row[self.SN] == serial_number:
                return False
    return True

```

##### **Explanation:**

Checks if a given serial number is unique in the 'assets.csv' file.

#### read_assets Method:

```py
def read_assets(self):
    # ... (prompting user for reading choice)
    if read_choice == "1":
        os.startfile("assets.csv")
        sys.exit()
    elif read_choice == "2":
        # ... (converting CSV to PDF and opening)
    elif read_choice == "3":
        # ... (reading and displaying assets in terminal)

``` 

##### **Explanation:**

Allows the user to choose how to view assets (spreadsheet, PDF, or default terminal view).
Logs the activity.

#### search_assets Method:

```py
def search_assets(self):
    # ... (prompting user for search criteria)
    try:
        with open('assets.csv', 'r', newline='') as csvfile:
            # ... (searching and displaying found assets)
    except FileNotFoundError:
        print("No assets found.\n")
    except KeyError:
        print("Entry can't be found or you mispelt an entry!")
        main()

```

##### **Explanation:**

Prompts the user for search criteria.
Searches assets based on the specified column and value.
Displays found assets in a tabulated format.
Logs the activity.
Handles FileNotFoundError and KeyError.

#### update_asset Method:

```py
def update_asset(self):
    # ... (prompting user for asset and update details)
    try:
        with open('assets.csv', 'r', newline='') as csvfile:
            # ... (updating the asset and logging the activity)
    except FileNotFoundError:
        print("No assets found.\n")

```

##### **Explanation:**

Prompts the user for the serial number and the field to update.
Updates the specified field of an asset.
Logs the old and new values.
Writes the updated assets to 'assets.csv'.
Handles FileNotFoundError.

#### delete_asset Method:

```py
def delete_asset(self):
    # ... (prompting user for asset details)
    try:
        with open('assets.csv', 'r', newline='') as csvfile:
            # ... (deleting the asset and logging the activity)
    except FileNotFoundError:
        print("No assets found.\n")

```

##### Explanation:

Prompts the user for the serial number of the asset to delete.
Deletes the specified asset.
Logs the deletion activity.
Writes the remaining assets to 'assets.csv'.
Handles FileNotFoundError.

#### User Manager Class (UserManager):

#### __init__ Method:

```py
def __init__(self):
    self.log_file = 'activity.log'

```

##### Explanation:

Initializes the UserManager with a log file.


#### log_activity Method:

```py
def log_activity(self, message):
    timestamp = datetime.now().strftime("%A, %Y-%m-%d %I:%M:%S %p")
    with open(self.log_file, 'a') as log_file:
        log_file.write(f"{timestamp} {message}\n")

```

##### Explanation:

Logs user activities with a timestamp.

#### login Method:

```py
def login(self, username, password):
    # ... (checks username and verifies password)
    return True/False

```

##### Explanation:

Authenticates a user by checking the username and password against stored data.
Logs successful logins.

#### create_account Method:

```py
def create_account(self, username, password):
    # ... (creates a new user account and logs the activity)
    return True/False

```

##### Explanation:

Creates a new user account.
Hashes the password before storing it.
Logs the account creation

#### hash_password Method:

```py
def hash_password(self, password):
    return hashlib.sha256(password.encode()).hexdigest()

```

##### Explanation:

Hashes a given password using SHA-256.

#### verify_password Method:

```py
def verify_password(self, stored_password, entered_password):
    return stored_password == self.hash_password(entered_password)

```

##### Explanation:

Verifies a password against a stored hashed password during login.

#### Display and Menu Functions:

```py
def print_yellow(text, rate=0.001):
    # ... (prints text in yellow with a specified printing rate)

```

##### Explanation:

Prints text in yellow with a specified printing rate.

#### display_menu Function:

```py
def display_menu():
    # ... (displays the main menu for login)

```

##### Explanation:

Displays the main menu for login.

#### login Function:

```py
def login(user_manager):
    # ... (takes user input for username and password)
    return True/False

```

##### Explanation:

Takes user input for username and password.
Calls user_manager.login for authentication.

#### create_user Function:

```py
def create_user(user_manager):
    # ... (takes user input for a new username and password)

```

##### Explanation:

Takes user input for a new username and password.
Calls user_manager.create_account to create a new user.

#### Main Execution (__name__ == "__main__"):

```py
if __name__ == "__main__":
    # ... (prints colorful ASCII art)
    user_manager = UserManager()
    while True:
        # ... (displays login menu and executes user choice)

```

##### Explanation:

Initializes the Asset Management System (asset_system).
Prints colorful ASCII art.
Loops through the main menu after a successful login.

## **Usage**

Run the program by executing ```python main.py```

Choose from the following options:

Create Asset (1): Enter details for a new asset.<br>
Read Assets (2): View a list of all assets.<br>
Update Asset (3): Modify details of an existing asset.<br>
Delete Asset (4): Remove a specific asset.<br>
Search Asset (5): Search for assets based on a specified criteria.<br>
Exit (6): Terminate the program.

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
