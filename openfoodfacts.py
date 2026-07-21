import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

def get_product_by_barcode(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    print("URL:", url)

    try:
        headers = {
    "User-Agent": "FoodInventoryApp/1.0 (student project)"
}

        response = requests.get(url, headers=headers)

        print("Status Code:", response.status_code)
        print("Response:", response.text[:300])  # Print the first 300 characters

        if response.status_code != 200:
            return None

        data = response.json()

        if data.get("status") != 1:
            return None

        product = data["product"]

        return {
            "product_name": product.get("product_name", "Unknown"),
            "brand": product.get("brands", "Unknown"),
            "ingredients": product.get("ingredients_text", "No ingredients listed")
        }

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
        return None
    
if __name__ == "__main__":
    barcode = "3017620422003"   # Nutella barcode

    product = get_product_by_barcode(barcode)

    print(product)