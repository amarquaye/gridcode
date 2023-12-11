import csv
import os
import sys
import logging
import hashlib
import time
from tabulate import tabulate
from datetime import datetime
from colorama import init, Fore, Style
from csv2pdf import convert
import pywriter as pw

init(autoreset=True)

class AssetManagementSystem:

    def __init__(self):
        # Check if the file exists
        self.file_exists = os.path.isfile('assets.csv')

        # Open the CSV file in append mode
        self.ID = 'ID'
        self.SN = 'SN'
        self.CATEGORY = 'CATEGORY'
        self.TYPE = 'TYPE'
        self.LOCATION = 'LOCATION'
        self.ASSIGNEE = 'ASSIGNEE'
        self.DESCRIPTION = 'DESCRIPTION'
        self.COLOR = 'COLOR'
        self.STATUS = 'STATUS'

        # Configure logging with custom format
        logging.basicConfig(filename='assets.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s: %(message)s',
                            datefmt='%A, %Y-%m-%d %I:%M:%S %p') 

    def log_activity(self, message):
        logging.info(message)

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

    def create_asset(self):
        print(f"{Fore.GREEN}Creating Asset{Style.RESET_ALL}")
        last_id = self.get_last_asset_id()
        new_id = last_id + 1

        ID = new_id

        print("NOTE, all entries will be converted to upper case automatically\n")

        if new_id > 1:
            while True:
                sn = input("Enter asset serial  number(SN): ")
                sn = sn.strip().upper()

                if self.is_serial_number_unique(sn):
                    break
                else:
                    print(f"Serial number '{sn}' already exists. Please enter a unique serial number.\n")
        else:
            sn = input("Enter asset serial  number(SN): ")
            sn = sn.strip().upper()

        asset_category = input("Enter asset category: ")
        asset_category = asset_category.strip().upper()

        asset_type = input("Enter asset type: ")
        asset_type = asset_type.strip().upper()

        location = input("Enter asset location: ")
        location = location.strip().upper()

        assignee = input("Enter the name of the person you want to assign this asset: ")
        assignee = assignee.strip().upper()
        if assignee == "":
            assignee = "NOT ASSIGNED"


        description = input("Enter a short description about the asset: ")
        description = description.strip().upper()

        color = input("Enter the color of the asset: ")
        color = color.strip().upper()

        status = input("Enter asset status: ")
        status = status.strip().upper()

        try:
            with open('assets.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=[self.ID, self.SN, self.CATEGORY, self.TYPE,
                                                             self.LOCATION, self.ASSIGNEE ,self.DESCRIPTION, self.COLOR, self.STATUS])

                # Check if the file is empty, and write the header only if it is
                if os.stat('assets.csv').st_size == 0:
                    writer.writeheader()

                # Write the new asset
                writer.writerow({self.ID: ID, self.SN: sn, self.CATEGORY: asset_category, self.TYPE: asset_type,
                                 self.LOCATION: location, self.ASSIGNEE: assignee, self.DESCRIPTION: description, self.COLOR: color, self.STATUS: status})

                # Log the activity
                log_message = f"Asset '{sn}' (ID: {ID}) added successfully."
                self.log_activity(log_message)

            print(f"Asset '{sn}' added successfully!\n")
        except PermissionError:
            print("Cannot access file\nPlease close your spreadsheet reader and try again!")

    def is_serial_number_unique(self, serial_number):
        with open('assets.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[self.SN] == serial_number:
                    return False
        return True

    def read_assets(self):
        print(f"{Fore.GREEN}Reading Assets{Style.RESET_ALL}")
        # List options
        print("\n1) Spread sheet")
        print("2) PDF")
        print("3) Default view(terminal)")

        read_choice = input("Enter the choice of reading: ")
        read_choice = read_choice.strip().upper()
        file_path = 'assets.csv'

        if read_choice == "1":
            #Logging Activity
            log_message = "Reading assets in spreadsheet."
            self.log_activity(log_message)
            # Open in spreadsheet form
            os.startfile("assets.csv")
            sys.exit()

        elif read_choice == "2":
            #Logging Activity
            log_message = "Reading assets in PDF."
            self.log_activity(log_message)

            try:
                convert("assets.csv", "assets.pdf", orientation="L")
            except Exception as e:
                print(f"Error {e}\nPlease terminate other instance of assest.pdf")
                
            # Open in PDF format
            os.startfile("assets.pdf")
            sys.exit()

        elif read_choice == "3":
            try:
                with open(file_path, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
        
                    # Assuming the first row contains headers
                    headers = next(csv_reader)
        
                    # Read data
                    data = [row for row in csv_reader]
        
                    # Print tabulated data
                    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


                    # Log the activity
                    log_message = "Read assets from the system."
                    self.log_activity(log_message)
                    print("\n")
            except FileNotFoundError:
                print("No assets found.\n")

        else:
            print("Invalid choice")

    def search_assets(self):
        print(f"{Fore.GREEN}Searching Assets{Style.RESET_ALL}")
        search_column = input("Enter the column to search in (ID / SN / CATEGORY / TYPE / LOCATION / ASSIGNEE / DESCRIPTION /COLOR / STATUS): ")
        search_column = search_column.strip().upper()

        search_value = input(f"Enter the value to search for in {search_column}: ")
        search_value = search_value.strip().upper()

        found_assets = []

        try:
            with open('assets.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    if row[search_column] == search_value:
                        found_assets.append(row)

                if found_assets:
                    headers = [self.ID, self.SN, self.CATEGORY, self.TYPE, self.LOCATION, self.ASSIGNEE, self.DESCRIPTION, self.COLOR, self.STATUS]
                    print("\nFound Assets:")
                    data = [
                        [found_asset[self.ID], found_asset[self.SN], found_asset[self.CATEGORY], found_asset[self.TYPE],
                         found_asset[self.LOCATION], found_asset[self.ASSIGNEE], found_asset[self.DESCRIPTION],
                         found_asset[self.COLOR], found_asset[self.STATUS]]
                        for found_asset in found_assets
                    ]
                    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
                    #Logging Activity
                    log_message = f"Found assets with {search_column} = {search_value}"
                    self.log_activity(log_message)
                else:
                    print(f"No assets found with {search_column} = {search_value}.\n")

        except FileNotFoundError:
            print("No assets found.\n")
        except KeyError:
            print("Entry can't be found or you mispelt an entry!")
            main()
        

    def update_asset(self):
        print(f"{Fore.GREEN}Updating Assets{Style.RESET_ALL}")
        sn = input("Enter the serial number of the asset you want to update: ")
        sn = sn.strip().upper()

        field_to_update = input(
            "Enter the field to update (SN / CATEGORY / TYPE / LOCATION / ASSIGNEE / DESCRIPTION /COLOR / STATUS): ")
        field_to_update = field_to_update.strip().upper()

        new_value = input(f"Enter the new value for {field_to_update}: ")
        new_value = new_value.strip().upper()

        rows = []
        updated = False

        try:
            with open('assets.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    if row[self.SN] == sn:
                        # Log the old values before updating
                        log_message_old = f"Asset '{sn}' (ID: {row[self.ID]}) - {field_to_update}: {row[field_to_update]} - updated to {new_value}."
                        self.log_activity(log_message_old)

                        row[field_to_update] = new_value
                        updated = True
                    rows.append(row)

            if updated:
                with open('assets.csv', 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=[self.ID, self.SN, self.CATEGORY, self.TYPE,
                                                                 self.LOCATION, self.ASSIGNEE ,self.DESCRIPTION, self.COLOR, self.STATUS])
                    writer.writeheader()
                    writer.writerows(rows)


                print(f"Asset '{sn}' updated to {new_value} successfully!\n")
            else:
                print(f"Asset '{sn}' not found.\n")

        except FileNotFoundError:
            print("No assets found.\n")

    def delete_asset(self):
        print(f"{Fore.GREEN}Deleting Assets{Style.RESET_ALL}")
        sn = input("Enter the serial number of the asset you want to delete: ")
        sn = sn.strip().upper()

        rows = []
        deleted = False

        try:
            with open('assets.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    if row[self.SN] == sn:
                        # Log the asset information before deleting
                        log_message = f"Asset '{sn}' (ID: {row[self.ID]}) deleted successfully."
                        self.log_activity(log_message)

                        deleted = True
                    else:
                        rows.append(row)

            if deleted:
                with open('assets.csv', 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=[self.ID, self.SN, self.CATEGORY, self.TYPE,
                                                                 self.LOCATION, self.ASSIGNEE ,self.DESCRIPTION, self.COLOR, self.STATUS])
                    writer.writeheader()
                    writer.writerows(rows)

                print(f"Asset '{sn}' deleted successfully!\n")
            else:
                print(f"Asset '{sn}' not found.\n")

        except FileNotFoundError:
            print("No assets found.\n")

init(autoreset=True)  # Initialize colorama

def print_yellow(text, rate=0.001):
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    for char in text:
        sys.stdout.write(YELLOW + char + RESET)
        sys.stdout.flush()
        time.sleep(rate)

class UserManager:
    def __init__(self):
        self.log_file = 'activity.log'

    def log_activity(self, message):
        timestamp = datetime.now().strftime("%A, %Y-%m-%d %I:%M:%S %p")
        with open(self.log_file, 'a') as log_file:
            log_file.write(f"{timestamp} {message}\n")

    def login(self, username, password):
        if os.path.exists('user_data.csv'):
            with open('user_data.csv', 'r', newline='') as csvfile:
                csvreader = csv.DictReader(csvfile)
                for row in csvreader:
                    if row['username'] == username and self.verify_password(row['password'], password):
                        log_message = f"'{username}' has logged in."
                        self.log_activity(log_message)
                        return True
        return False

    def create_account(self, username, password):
        fieldnames = ['username', 'password']

        if not os.path.exists('user_data.csv'):
            with open('user_data.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
                writer.writeheader()

        hashed_password = self.hash_password(password)

        with open('user_data.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
            writer.writerow({'username': username, 'password': hashed_password})
            log_message = f"Account created for user '{username}'."
            self.log_activity(log_message)
            return True

    def hash_password(self, password):
        # Use a secure hashing algorithm (e.g., SHA-256) for password hashing
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, stored_password, entered_password):
        # Compare hashed passwords during login verification
        return stored_password == self.hash_password(entered_password)

def display_menu():
    print("\n" + "=" * 30)
    print(f"{Fore.CYAN}Welcome to Console Login{Style.RESET_ALL}")
    print("=" * 30)
    print("1. Login")
    print("2. Create User")
    print("3. Exit")

def login(user_manager):
    print("\n" + "=" * 30)
    print(f"{Fore.YELLOW}Login{Style.RESET_ALL}")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Dummy authentication (replace with your authentication logic)
    if user_manager.login(username, password):
        print(f"{Fore.GREEN}Login successful!{Style.RESET_ALL}")
        return True
    else:
        print(f"{Fore.RED}Login failed. Invalid username or password.{Style.RESET_ALL}")
        return False

def create_user(user_manager):
    print("\n" + "=" * 30)
    print(f"{Fore.YELLOW}Create User{Style.RESET_ALL}")
    new_username = input("Enter a new username: ")
    new_password = input("Enter a new password: ")

    # Dummy storage (replace with your user creation logic)
    # Here, we are storing the username and a hash of the password.
    # In a real application, use a secure storage mechanism.
    if user_manager.create_account(new_username, new_password):
        print(f"{Fore.GREEN}User created successfully!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Failed to create user.{Style.RESET_ALL}")


# Main function
def main():
    asset_system = AssetManagementSystem()

    while True:
        print("\n" + "=" * 30)
        print(f"{Fore.CYAN}Asset Management System{Style.RESET_ALL}")
        print("=" * 30)
        print("1. Create Asset")
        print("2. Read Assets")
        print("3. Update Asset")
        print("4. Delete Asset")
        print("5. Search Asset")
        print("6) Exit")

        choice = input("Enter your choice (1-6): ")
        choice = choice.strip()

        if choice == '1':
            asset_system.create_asset()
        elif choice == '2':
            asset_system.read_assets()
        elif choice == '3':
            asset_system.update_asset()
        elif choice == '4':
            asset_system.delete_asset()
        elif choice == '5':
            asset_system.search_assets()
        elif choice == '6':

            confirm = input("Are you sure you want to exit this application? [Y/N]: ")
            if confirm.strip().upper() == "Y":
                print(f"{Fore.CYAN}Exiting the Asset Management System. Goodbye!{Style.RESET_ALL}\n")
                print(f"{Fore.YELLOW}AMS, powered by GridCode.{Style.RESET_ALL}")
                break
            elif confirm.strip().upper() == "N":
                main()
            else:
                print(f"{Fore.RED}Invalid response, {confirm}{Style.RESET_ALL}\n")
                main()
        else:
            print(f"{Fore.RED}Invalid choice. Please enter a number between 1 and 6.{Style.RESET_ALL}\n")


if __name__ == "__main__":
    
    text_to_print=r""""
  ,----..           ,-.----.              ,---,            ,---,              ,----..             /   /   \              ,---,                ,---,. 
 /   /   \          \    /  \          ,`--.' |          .'  .' `\           /   /   \           /   .     :           .'  .' `\            ,'  .' | 
|   :     :         ;   :    \         |   :  :        ,---.'     \         |   :     :         .   /   ;.  \        ,---.'     \         ,---.'   | 
.   |  ;. /         |   | .\ :         :   |  '        |   |  .`\  |        .   |  ;. /        .   ;   /  ` ;        |   |  .`\  |        |   |   .' 
.   ; /--`          .   : |: |         |   :  |        :   : |  '  |        .   ; /--`         ;   |  ; \ ; |        :   : |  '  |        :   :  |-, 
;   | ;  __         |   |  \ :         '   '  ;        |   ' '  ;  :        ;   | ;            |   :  | ; | '        |   ' '  ;  :        :   |  ;/| 
|   : |.' .'        |   : .  /         |   |  |        '   | ;  .  |        |   : |            .   |  ' ' ' :        '   | ;  .  |        |   :   .' 
.   | '_.' :        ;   | |  \         '   :  ;        |   | :  |  '        .   | '___         '   ;  \; /  |        |   | :  |  '        |   |  |-, 
'   ; : \  |        |   | ;\  \        |   |  '        '   : | /  ;         '   ; : .'|         \   \  ',  /         '   : | /  ;         '   :  ;/| 
'   | '/  .'        :   ' | \.'        '   :  |        |   | '` ,/          '   | '/  :          ;   :    /          |   | '` ,/          |   |    \ 
|   :    /          :   : :-'          ;   |.'         ;   :  .'            |   :    /            \   \ .'           ;   :  .'            |   :   .' 
 \   \ .'           |   |.'            '---'           |   ,.'               \   \ .'              `---`             |   ,.'              |   | ,'   
  `---`             `---'                              '---'                  `---`                                  '---'                `----'     
"""
    print_yellow(text_to_print, rate=0.001)


    user_manager = UserManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            if login(user_manager):
                # Continue to display menu after successful login
                main()
        elif choice == "2":
            create_user(user_manager)
        elif choice == "3":
            print(f"{Fore.CYAN}Exiting. Goodbye!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter a valid option.{Style.RESET_ALL}")
