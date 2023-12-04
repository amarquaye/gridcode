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
        sn = sn.upper().strip()

        asset_category = input("Enter asset category: ")
        asset_category = asset_category.upper().strip()

        asset_type = input("Enter asset type: ")
        asset_type = asset_type.upper().strip()

        location = input("Enter asset location: ")
        location = location.upper().strip()

        description = input("Enter a short description about the asset: ")
        description = description.upper().strip()

        color = input("Enter the color of the asset: ")
        color = color.upper().strip()

        status = input("Enter asset status: ")
        status = status.upper().strip()

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

    def read_assets(self):
        try:
            with open('assets.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                print("\nList of Assets:")
                for row in reader:
                    print(
                        f"ID: {row['ID']}, SN: {row['SN']}, CATEGORY: {row['CATEGORY']}, TYPE: {row['TYPE']}, LOCATION: {row['LOCATION']}, DESCRIPTION: {row['DESCRIPTION']}, COLOR: {row['COLOR']}, STATUS: {row['STATUS']}")
                print("\n")
        except FileNotFoundError:
            print("No assets found.\n")

    def update_asset(self):
        sn = input("Enter the serial number of the asset you want to update: ")
        field_to_update = input(
            "Enter the field to update (SN / CATEGORY / TYPE / LOCATION / DESCRIPTION /COLOR / STATUS): ")
        new_value = input(f"Enter the new value for {field_to_update}: ")

        rows = []
        updated = False

        try:
            with open('assets.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    if row['SN'] == sn:
                        row[field_to_update] = new_value
                        updated = True
                    rows.append(row)

            if updated:
                with open('assets.csv', 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                print(f"Asset '{sn}' updated to {new_value} successfully!\n")
            else:
                print(f"Asset '{sn}' not found.\n")

        except FileNotFoundError:
            print("No assets found.\n")

    def delete_asset(self):
        sn = input("Enter the serial number of the asset you want to delete: ")

        rows = []
        deleted = False

        try:
            with open('assets.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    if row['SN'] == sn:
                        deleted = True
                    else:
                        rows.append(row)

            if deleted:
                with open('assets.csv', 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
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

        if choice == '1':
            asset_system.create_asset()
        elif choice == '2':
            asset_system.read_assets()
        elif choice == '3':
            asset_system.update_asset()
        elif choice == '4':
            asset_system.delete_asset()
        elif choice == '5':

            confirm = input("Are you sure you want to exit this application?[Y/N] ")
            if confirm.upper() == "Y":
                print("Exiting the Asset Management System. Goodbye!\n")
                print("AMS, powered by GridCode.")
                sys.exit()
            elif confirm.upper() == "N":
                main()
            else:
                print(f"Invalid response, {confirm}\n")
                main()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
