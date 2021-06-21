
class Products:
    def __init__(self):
        self.product = {
            "name": "Colombian Jersey",
            "type": "simple",
            "regular_price": "100.00",
            "description": "Official Colombian Jersey from the Copa America 2021.",
            "short_description": "",
            "categories": [
                    {
                        "id": 18
                    }
            ],
            "images": [
                {
                    "src": "https://todosobrecamisetas.com/wp-content/uploads/camiseta-adidas-colombia-2021-2.jpg"
                },
                {
                    "src": "https://todosobrecamisetas.com/wp-content/uploads/camiseta-adidas-colombia-2021-3.jpg"
                }
            ]
        }

    def get_product(self, wcapi, productID):
        """
        This method gets a specific product based on its ID
        :param wcapi: The API session
        :param productID: The product ID to be retrieved
        return: The response from the API that contains the information of the retrieved product and API response status code
        """
        product = wcapi.get("products/"+str(productID))
        return product

    def create_product(self, wcapi):
        """
        This method creates a product based on the data in the attribute product
        :param wcapi: The API session
        return: The response from the API that contains the information of the created product and API response status code
        """
        newProduct = wcapi.post("products", self.product)
        return newProduct

    def delete_product(self, wcapi, verifyID):
        """
        This method deletes a specific product based on the product's id
        :param wcapi: The API session
        :param verifyID: The product's id to be deleted
        return: The response from the API that contains the information of the deleted and API response status code
        """
        deletedProduct = wcapi.delete("products/"+str(verifyID),
                                      params={"force": True})
        return deletedProduct

    def get_all_products(self, wcapi):
        """
        This method gets the list of all available products in the application
        :param wcapi: The API session
        return: The response from the API that contains the information of the products and API response status code
        """
        allProducts = wcapi.get("products")
        return allProducts
