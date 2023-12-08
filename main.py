import csv
import os
import sys
import logging
from datetime import datetime 
from csv2pdf import convert
import pywriter as pw


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
        last_id = self.get_last_asset_id()
        new_id = last_id + 1

        ID = new_id

        print("NOTE, all entries will be converted to upper case automatically\n")

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

    def read_assets(self):
        # List options
        print("\n1) Spread sheet")
        print("2) PDF")
        print("3) Default view(terminal)")

        read_choice = input("Enter the choice of reading: ")
        read_choice = read_choice.strip().upper()

        if read_choice == "1":
            # Open in spreadsheet form
            os.startfile("assets.csv")
            sys.exit()

        elif read_choice == "2":
            convert("assets.csv", "assets.pdf", orientation="L")
            # Open in PDF format
            os.startfile("assets.pdf")
            sys.exit()

        elif read_choice == "3":
            try:
                with open('assets.csv', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    print("\nList of Assets:")
                    for row in reader:
                        print(
                            f"ID: {row[self.ID]}, SN: {row[self.SN]}, CATEGORY: {row[self.CATEGORY]}, TYPE: {row[self.TYPE]}, "
                            f"LOCATION: {row[self.LOCATION]}, ASSIGNEE: {row[self.ASSIGNEE]}, DESCRIPTION: {row[self.DESCRIPTION]}, COLOR: {row[self.COLOR]}, "
                            f"STATUS: {row[self.STATUS]}")

                    # Log the activity
                    log_message = "Read assets from the system."
                    self.log_activity(log_message)

                    print("\n")
            except FileNotFoundError:
                print("No assets found.\n")

        else:
            print("Invalid choice")

    def search_assets(self):
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
                    print("\nFound Assets:")
                    for found_asset in found_assets:
                        print(
                            f"ID: {found_asset[self.ID]}, SN: {found_asset[self.SN]}, CATEGORY: {found_asset[self.CATEGORY]}, TYPE: {found_asset[self.TYPE]}, "
                            f"LOCATION: {found_asset[self.LOCATION]}, ASSIGNEE: {found_asset[self.ASSIGNEE]}, DESCRIPTION: {found_asset[self.DESCRIPTION]}, COLOR: {found_asset[self.COLOR]}, "
                            f"STATUS: {found_asset[self.STATUS]}")
                else:
                    print(f"No assets found with {search_column} = {search_value}.\n")

        except FileNotFoundError:
            print("No assets found.\n")
        except KeyError:
            print("Entry can't be found or you mispelt an entry!")
            main()
        

    def update_asset(self):
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

def log_in():
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    if user_manager.login(username_input, password_input):
        print("Login successful!")
        main()
    else:
        print("Login failed.")

class UserManager:
    def __init__(self):
        self.log_file = 'activity_log.txt'

    def log_activity(self, message):
        timestamp = datetime.now().strftime("%A, %Y-%m-%d %I:%M:%S %p")
        with open(self.log_file, 'a') as log_file:
            log_file.write(f"{timestamp} {message}\n")

    def login(self, username, password):
        if os.path.exists('user_data.csv'):
            with open('user_data.csv', 'r', newline='') as csvfile:
                csvreader = csv.DictReader(csvfile)
                for row in csvreader:
                    if row['username'] == username and row['password'] == password:
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

        with open('user_data.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
            writer.writerow({'username': username, 'password': password})
            log_message = f"Account created for user '{username}'."
            self.log_activity(log_message)
            return True


# Main function
def main():
    asset_system = AssetManagementSystem()

    while True:
        print("\nAsset Management System")
        print("1. Create Asset")
        print("2. Read Assets")
        print("3. Update Asset")
        print("4. Delete Asset")
        print("5. Search Asset")
        print("6) Exit")

        choice = input("Enter your choice (1-5): ")
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
                print("Exiting the Asset Management System. Goodbye!\n")
                print("AMS, powered by GridCode.")
                sys.exit()
            elif confirm.strip().upper() == "N":
                main()
            else:
                print(f"Invalid response, {confirm}\n")
                main()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    
    pw.write(rate=0.001, text=r""""
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
""")

    user_manager = UserManager()

    # Login
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    if user_manager.login(username_input, password_input):
        print("Login successful!")
        main()
    else:
        print("Login failed.")
        ans = input("Would you like to create an account?[Y/N]")
        if ans.strip().upper() == "Y":
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            if user_manager.create_account(new_username, new_password):
                print("Account created!") 
                log_in()
            else:
                print("Failed to create an account.")
        else:
            print("Alright! Thank you for coming.")
            sys.exit()
