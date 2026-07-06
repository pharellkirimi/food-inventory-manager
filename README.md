# Food Inventory Manager

## Description

Food Inventory Manager is a Flask REST API that manages food products in an inventory. It uses an in-memory list as a temporary database and connects to the OpenFoodFacts API to retrieve product information using a barcode. A CLI application is included to interact with the API.

## Features

* View all products
* View a single product
* Add a product
* Update product price and stock
* Delete a product
* Search products using the OpenFoodFacts API
* Unit tests using `pytest`

## Installation

1. Clone the repository.

```bash
git clone https://github.com/pharellkirimi/food-inventory-manager.git
```

2. Move into the project folder.

```bash
cd food-inventory-manager
```

3. Install the required packages.

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

Run the CLI in another terminal:

```bash
python cli.py
```

## API Endpoints

| Method | Endpoint            | Description          |
| ------ | ------------------- | -------------------- |
| GET    | `/inventory`        | Get all products     |
| GET    | `/inventory/<id>`   | Get one product      |
| POST   | `/inventory`        | Add a product        |
| PATCH  | `/inventory/<id>`   | Update a product     |
| DELETE | `/inventory/<id>`   | Delete a product     |
| GET    | `/search/<barcode>` | Search OpenFoodFacts |

## Example POST Request

```json
{
  "barcode": "3017620422003",
  "price": 12.99,
  "stock": 30
}
```

## Running Tests

Run all tests with:

```bash
pytest
```

## Technologies

* Python
* Flask
* Requests
* Pytest
* OpenFoodFacts API
# food-inventory-manager
