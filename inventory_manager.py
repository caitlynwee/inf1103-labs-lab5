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