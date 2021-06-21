import pytest
import requests
import json
from lib.coupons import Coupons
from woocommerce import API

global COUPONID


wcapi = API(
    url="http://localhost:8000",
    consumer_key="ck_747561c1957b4d5e9c4ba174397365f9bdf43ab7",
    consumer_secret="cs_ae256b8de43dd771568cab572c8c135b11ff21f3",
    timeout=50
)


def test_get_all_coupons():

    response = Coupons().get_all_coupons(wcapi)
    assert response.ok


def test_create_coupon():

    response = Coupons().create_coupon(wcapi)
    assert response.ok
    global COUPONID
    COUPONID = response.json()['id']
    couponCode = response.json()['code']
    assert couponCode == Coupons().coupon['code'], 'Verify coupon was created'


def test_delete_created_coupon():
    response = Coupons().delete_coupon(wcapi, COUPONID)
    assert response.ok
