from unittest.mock import patch
from openfoodfacts import get_product_by_barcode


@patch("openfoodfacts.requests.get")
def test_get_product(mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Nutella",
            "brands": "Ferrero",
            "ingredients_text": "Sugar, Hazelnuts"
        }
    }

    product = get_product_by_barcode("3017620422003")

    assert product["product_name"] == "Nutella"
    assert product["brand"] == "Ferrero"