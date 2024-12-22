# E-commerce API

This is a RESTful API for an e-commerce platform, built with Flask, SQLAlchemy, and Marshmallow. It includes endpoints for managing users, products, and orders.

## Features

- **User Management**: Create, retrieve, update, and delete user information.
- **Product Management**: Create, retrieve, update, and delete product information.
- **Order Management**: Create orders, add or remove products from orders, and retrieve orders and related products.

## Getting Started

### Prerequisites

- Python 3.6+
- MySQL
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- Marshmallow-SQLAlchemy
- SQLAlchemy
- MySQL Connector

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Rigil87/Ecommerce-API.git
    cd your-repository
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up MySQL database:**

   Ensure you have MySQL installed and running. Create a database for your project.

    ```sql
    CREATE DATABASE ecommerce_api;
    ```

5. **Update configuration:**

   Update your `app.py` with the correct MySQL connection string.

    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/ecommerce_api'
    ```

6. **Run the application:**

    ```bash
    python server.py
    ```

## API Endpoints

### User Endpoints

- **GET /users**: Retrieve all users
- **GET /users/<id>**: Retrieve a user by ID
- **POST /users**: Create a new user
- **PUT /users/<id>**: Update a user by ID
- **DELETE /users/<id>**: Delete a user by ID

### Product Endpoints

- **GET /products**: Retrieve all products
- **GET /products/<id>**: Retrieve a product by ID
- **POST /products**: Create a new product
- **PUT /products/<id>**: Update a product by ID
- **DELETE /products/<id>**: Delete a product by ID

### Order Endpoints

- **POST /orders**: Create a new order (requires user ID and order date)
- **GET /orders/<order_id>/add_product/<product_id>**: Add a product to an order (prevent duplicates)
- **DELETE /orders/<order_id>/remove_product/<product_id>**: Remove a product from an order
- **GET /orders/user/<user_id>**: Get all orders for a user
- **GET /orders/<order_id>/products**: Get all products for an order

## Testing

1. **Run Database Setup:**

   Ensure that calling `db.create_all()` creates all required tables in MySQL.

2. **Use Postman:**

   Create a Postman collection and add a request for each of your API endpoints to the collection. Then export the collection and include it in your project folder.

3. **Verify Data:**

   Use MySQL Workbench to ensure data is being correctly stored in the database.

## Contributing

If you wish to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

Developed with 💙 by Travis Locke
