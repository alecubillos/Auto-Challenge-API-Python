
import requests


class Coupons:
    def __init__(self):
        self.coupon = {
            "code": "60off",
            "discount_type": "percent",
            "amount": "60",
            "individual_use": True,
            "exclude_sale_items": True,
            "minimum_amount": "75.00"
        }

    def get_all_coupons(self, wcapi):
        """
        This method gets all the coupons available in the application
        :param wcapi: The API session
        return: The response from the API that contains all the coupons and API response status code
        """
        allCoupons = wcapi.get("coupons")
        return allCoupons

    def create_coupon(self, wcapi):
        """
        This method creates a coupon with the data from the attribute coupon
        :param wcapi: The API session
        return: The response from the API that contains the information of the newly created coupon and API response status code
        """
        newCoupon = wcapi.post("coupons", self.coupon)
        return newCoupon

    def delete_coupon(self, wcapi, couponID):
        """
        This method deletes a specific coupon based on its ID
        :param wcapi: The API session
        :param couponID: The couponID to be deleted
        return: The response from the API that contains the information of the deleted coupon and API response status code
        """
        deletedCoupon = wcapi.delete(
            "coupons/"+str(couponID), params={"force": True})
        return deletedCoupon
