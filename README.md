# Auto-Challenge-API-Python
This project automates manual API test cases for an e-commerce application

1. Create a product
2. Create a Coupon
3. Place an order using a discount coupon

Teardown:
1. Delete the created product
2. Delete the created Coupon
3. Delete the created Order

#To Run All the Tests at Once
1. Open the terminal and execute the command: pytest tests

#To Ruun a Specific Test
1. Open the terminal and execute the command: pytest tests/<test_name.py>
i.e: To run the tests for products: pytest tests/test_products.py

