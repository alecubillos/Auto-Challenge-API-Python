import requests


class Orders:
    def __init__(self):
        self.order = {
            "payment_method": "bacs",
            "payment_method_title": "Direct Bank Transfer",
            "set_paid": True,
            "billing": {
                "first_name": "Alejandra",
                "last_name": "Cubillos",
                "address_1": "Apto 1203",
                "address_2": "",
                "city": "Medellin",
                "state": "Antioquia",
                "postcode": "94103",
                "country": "Colombia",
                "email": "ale.cubillos@example.com",
                "phone": "(555) 555-5555"
            },
            "shipping": {
                "first_name": "Alejandra",
                "last_name": "Cubillos",
                "address_1": "969 Market",
                "address_2": "",
                "city": "Medellin",
                "state": "Antioquia",
                "postcode": "94103",
                "country": "Colombia"
            },
            "line_items": [
                {
                    "product_id": 39,
                    "quantity": 5
                }],
            "shipping_lines": [
                {
                    "method_id": "flat_rate",
                    "method_title": "Flat Rate",
                    "total": "10.00"
                }
            ],
            "coupon_lines": [
                {
                    "id": 206,
                    "code": '50off',
                    "discount": "100.00"

                }]
        }

    def create_order_with_coupon(self, wcapi):
        """
        This method creates an order based on the data in the attribute order
        :param wcapi: The API session
        return: The response from the API that contains the information of the created order and API response status code
        """
        order = wcapi.post("orders", self.order)
        return order

    def delete_order(self, wcapi, orderID):
        """
        This method deletes a specific order based on the order's id
        :param wcapi: The API session
        :param orderID: order's id to be deleted
        return: The response from the API that contains the information of the deleted order and API response status code
        """
        deletedOrder = wcapi.delete(
            "orders/"+str(orderID), params={"force": True})
        return deletedOrder
