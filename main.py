import csv
import os
import sys
import logging


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

        description = input("Enter a short description about the asset: ")
        description = description.strip().upper()

        color = input("Enter the color of the asset: ")
        color = color.strip().upper()

        status = input("Enter asset status: ")
        status = status.strip().upper()

        with open('assets.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[self.ID, self.SN, self.CATEGORY, self.TYPE,
                                                         self.LOCATION, self.DESCRIPTION, self.COLOR, self.STATUS])

            # Check if the file is empty, and write the header only if it is
            if os.stat('assets.csv').st_size == 0:
                writer.writeheader()

            # Write the new asset
            writer.writerow({self.ID: ID, self.SN: sn, self.CATEGORY: asset_category, self.TYPE: asset_type,
                             self.LOCATION: location, self.DESCRIPTION: description, self.COLOR: color, self.STATUS: status})

            # Log the activity
            log_message = f"Asset '{sn}' (ID: {ID}) added successfully."
            self.log_activity(log_message)

        print(f"Asset '{sn}' added successfully!\n")

    def read_assets(self):
        try:
            with open('assets.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                print("\nList of Assets:")
                for row in reader:
                    print(
                        f"ID: {row[self.ID]}, SN: {row[self.SN]}, CATEGORY: {row[self.CATEGORY]}, TYPE: {row[self.TYPE]}, "
                        f"LOCATION: {row[self.LOCATION]}, DESCRIPTION: {row[self.DESCRIPTION]}, COLOR: {row[self.COLOR]}, "
                        f"STATUS: {row[self.STATUS]}")

                # Log the activity
                log_message = "Read assets from the system."
                self.log_activity(log_message)

                print("\n")
        except FileNotFoundError:
            print("No assets found.\n")

    def update_asset(self):
        sn = input("Enter the serial number of the asset you want to update: ")
        sn = sn.strip().upper()

        field_to_update = input(
            "Enter the field to update (SN / CATEGORY / TYPE / LOCATION / DESCRIPTION /COLOR / STATUS): ")
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
                                                                 self.LOCATION, self.DESCRIPTION, self.COLOR, self.STATUS])
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
                                                                 self.LOCATION, self.DESCRIPTION, self.COLOR, self.STATUS])
                    writer.writeheader()
                    writer.writerows(rows)

                print(f"Asset '{sn}' deleted successfully!\n")
            else:
                print(f"Asset '{sn}' not found.\n")

        except FileNotFoundError:
            print("No assets found.\n")
# Main function
def main():
    asset_system = AssetManagementSystem()

    while True:
        print("\nAsset Management System")
        print("1. Create Asset")
        print("2. Read Assets")
        print("3. Update Asset")
        print("4. Delete Asset")
        print("5. Exit")

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
    main()
