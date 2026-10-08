import json
import os

FILE_NAME = "inventory.json"

def load_inventory():
    """
    Load inventory data from inventory.json.

    If inventory.json does not exist,
    create a default inventory with 3 products.
    """

    if os.path.exists(FILE_NAME):
        print("inventory.json found.")

        try:
            with open(FILE_NAME, "r") as file:
                inventory = json.load(file)

            print("Inventory loaded successfully.")
            return inventory

        except json.JSONDecodeError:
            print("Error: inventory.json contains invalid JSON.")
            print("Starting with an empty inventory.")
            return []

        except Exception as error:
            print(f"Error loading inventory: {error}")
            return []

    else:
        print("inventory.json not found.")
        print("Creating default inventory.")

        inventory = [
            {
                "id": "P001",
                "name": "Laptop",
                "price": 1200.00,
                "stock": 15
            },
            {
                "id": "P002",
                "name": "Mouse",
                "price": 25.50,
                "stock": 40
            },
            {
                "id": "P003",
                "name": "Keyboard",
                "price": 45.00,
                "stock": 25
            }
        ]
        return inventory

def save_inventory(inventory):
    """
    Save inventory data into inventory.json.
    """

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(inventory, file, indent=4)

        print("Inventory saved successfully to inventory.json.")

    except Exception as error:
        print(f"Error saving inventory: {error}")

def display_all(inventory):
    """
    Display every product currently stored
    in the inventory.
    """

    print("\nCurrent Inventory")
    print("------------------------------------------------")

    if len(inventory) == 0:
        print("Inventory is empty.")

    else:
        for product in inventory:
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )

    print("------------------------------------------------")
    
def add_product(inventory):
    """
    Add a new product into the inventory.
    """

    print("\nAdd New Product")

    product_id = input("Product ID: ").strip().upper()

    for product in inventory:
        if product["id"].upper() == product_id:
            print("Error: Product ID already exists.")
            return

    product_name = input("Product Name: ").strip()

    while True:
        try:
            price = float(input("Price: "))

            if price < 0:
                print("Price cannot be negative.")
                continue

            break

        except ValueError:
            print("Invalid price. Please enter a number.")

    while True:
        try:
            stock = int(input("Stock Quantity: "))

            if stock < 0:
                print("Stock quantity cannot be negative.")
                continue

            break

        except ValueError:
            print("Invalid stock quantity. Please enter a whole number.")

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)

    print("Product added successfully!")
    
def update_stock(inventory):
    """
    Search for a product by ID
    and update its stock quantity.
    """

    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip().upper()

    for product in inventory:

        if product["id"].upper() == product_id:

            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            while True:
                try:
                    new_stock = int(input("New Stock Quantity: "))

                    if new_stock < 0:
                        print("Stock quantity cannot be negative.")
                        continue

                    break

                except ValueError:
                    print(
                        "Invalid stock quantity. "
                        "Please enter a whole number."
                    )

            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")
    
def search_product(inventory):
    """
    Search for and display one product
    using its product ID.
    """

    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip().upper()

    for product in inventory:

        if product["id"].upper() == product_id:

            print("Product Found")
            print("------------------------------------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("------------------------------------------------")

            return

    print("Product not found.")

def display_menu():
    """
    Display the main inventory menu.
    """

    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

def main():

    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    # Load inventory when program starts
    inventory = load_inventory()

    while True:

        display_menu()

        option = input("Enter option: ").strip()

        # Option 1 - Display
        if option == "1":
            display_all(inventory)

        # Option 2 - Add
        elif option == "2":
            add_product(inventory)

        # Option 3 - Update
        elif option == "3":
            update_stock(inventory)

        # Option 4 - Search
        elif option == "4":
            search_product(inventory)

        # Option 5 - Save
        elif option == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)

        # Option 6 - Exit
        elif option == "6":

            print("\nSaving inventory before exit...")

            try:
                with open(FILE_NAME, "w") as file:
                    json.dump(inventory, file, indent=4)

                print("Inventory saved successfully.")

            except Exception as error:
                print(f"Error saving inventory: {error}")

            print("Thank you for using Inventory Management System.")
            print("Program terminated.")

            break

        # Invalid menu input
        else:
            print("Invalid option. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()