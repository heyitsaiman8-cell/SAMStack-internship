import json
import os


FILE_NAME = "inventory.json"


def load_inventory():

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Error reading inventory file.")
        return []


def save_inventory(inventory):
   
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(inventory, file, indent=4)
    except OSError:
        print("Error saving inventory.")


def get_valid_integer(message, minimum=None):
   
    while True:
        try:
            value = int(input(message))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_float(message, minimum=None):
    
    while True:
        try:
            value = float(input(message))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid price.")


def display_inventory(inventory):
    
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\n========== INVENTORY ==========")

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: {product['price']:.2f} | "
            f"Quantity: {product['quantity']}"
        )


def add_product(inventory):
    
    print("\n========== ADD PRODUCT ==========")

    product_id = get_valid_integer("Enter product ID: ", 1)

    for product in inventory:
        if product["id"] == product_id:
            print("Product ID already exists.")
            return

    name = input("Enter product name: ").strip()

    if not name:
        print("Product name cannot be empty.")
        return

    price = get_valid_float("Enter product price: ", 0.01)
    quantity = get_valid_integer("Enter product quantity: ", 1)

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)
    save_inventory(inventory)

    print("Product added successfully.")


def update_product(inventory):
    
    print("\n========== UPDATE PRODUCT ==========")

    product_id = get_valid_integer("Enter product ID: ", 1)

    for product in inventory:
        if product["id"] == product_id:
            print(f"Current name: {product['name']}")
            print(f"Current price: {product['price']}")
            print(f"Current quantity: {product['quantity']}")

            new_name = input(
                "Enter new name (press Enter to keep current): "
            ).strip()

            if new_name:
                product["name"] = new_name

            new_price = get_valid_float(
                "Enter new price: ",
                0.01
            )

            new_quantity = get_valid_integer(
                "Enter new quantity: ",
                0
            )

            product["price"] = new_price
            product["quantity"] = new_quantity

            save_inventory(inventory)

            print("Product updated successfully.")
            return

    print("Product not found.")


def remove_product(inventory):
    
    print("\n========== REMOVE PRODUCT ==========")

    product_id = get_valid_integer("Enter product ID: ", 1)

    for product in inventory:
        if product["id"] == product_id:
            inventory.remove(product)
            save_inventory(inventory)

            print("Product removed successfully.")
            return

    print("Product not found.")


def create_bill(inventory):
   
    print("\n========== CREATE BILL ==========")

    if not inventory:
        print("Inventory is empty.")
        return

    bill_items = []
    total = 0

    while True:
        display_inventory(inventory)

        product_id = get_valid_integer(
            "\nEnter product ID (0 to finish): ",
            0
        )

        if product_id == 0:
            break

        selected_product = None

        for product in inventory:
            if product["id"] == product_id:
                selected_product = product
                break

        if selected_product is None:
            print("Product not found.")
            continue

        quantity = get_valid_integer(
            "Enter quantity: ",
            1
        )

        if quantity > selected_product["quantity"]:
            print(
                f"Insufficient stock. "
                f"Available: {selected_product['quantity']}"
            )
            continue

        subtotal = selected_product["price"] * quantity

        bill_items.append(
            {
                "name": selected_product["name"],
                "price": selected_product["price"],
                "quantity": quantity,
                "subtotal": subtotal
            }
        )

        selected_product["quantity"] -= quantity
        total += subtotal

        print("Product added to bill.")

    if not bill_items:
        print("No items purchased.")
        return

    save_inventory(inventory)

    print("\n========== FINAL BILL ==========")

    for item in bill_items:
        print(
            f"{item['name']} x {item['quantity']} "
            f"= {item['subtotal']:.2f}"
        )

    print("-------------------------------")
    print(f"TOTAL: {total:.2f}")
    print("===============================")


def main():
    """Run the Inventory and Billing System."""
    inventory = load_inventory()

    while True:
        print("\n")
        print("-----------Main Block-----------")
        print("---------------of-------------")
        print("----------inventory system-----------")
        print("================================")
        print("   INVENTORY & BILLING SYSTEM")
        print("================================")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Remove Product")
        print("5. Create Bill")
        print("6. Exit")
        print("================================")

        choice = get_valid_integer(
            "Enter your choice: ",
            1
        )

        if choice == 1:
            display_inventory(inventory)

        elif choice == 2:
            add_product(inventory)

        elif choice == 3:
            update_product(inventory)

        elif choice == 4:
            remove_product(inventory)

        elif choice == 5:
            create_bill(inventory)

        elif choice == 6:
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()