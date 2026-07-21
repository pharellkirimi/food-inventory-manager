import requests

BASE_URL = "http://127.0.0.1:5000"


def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        products = response.json()

        print("\n===== Inventory =====")

        for product in products:
            print(
                f"\nID: {product['id']}"
                f"\nName: {product['product_name']}"
                f"\nPrice: ${product['price']}"
                f"\nStock: {product['stock']}"
            )
    else:
        print("Unable to retrieve inventory.")


def view_product():
    item_id = input("Enter Product ID: ")

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        product = response.json()

        print("\n===== Product Details =====")
        print(f"ID: {product['id']}")
        print(f"Barcode: {product['barcode']}")
        print(f"Name: {product['product_name']}")
        print(f"Brand: {product['brand']}")
        print(f"Ingredients: {product['ingredients']}")
        print(f"Price: ${product['price']}")
        print(f"Stock: {product['stock']}")
    else:
        print(response.json()["error"])


def add_product():
    barcode = input("Barcode: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))

    data = {
        "barcode": barcode,
        "price": price,
        "stock": stock
    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=data
    )

    print(response.json())


def update_product():
    item_id = input("Product ID: ")

    price = float(input("New Price: "))
    stock = int(input("New Stock: "))

    data = {
        "price": price,
        "stock": stock
    }

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=data
    )

    print(response.json())


def delete_product():
    item_id = input("Product ID: ")

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    print(response.json())


def search_product():
    barcode = input("Barcode: ")

    response = requests.get(
        f"{BASE_URL}/search/{barcode}"
    )

    print(response.json())


def main():
    while True:

        print("\n==============================")
        print(" FOOD INVENTORY MANAGER")
        print("==============================")
        print("1. View Inventory")
        print("2. View Product")
        print("3. Add Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Find Product on API")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            view_product()

        elif choice == "3":
            add_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            search_product()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()