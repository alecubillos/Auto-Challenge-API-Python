import pytest
import requests
import json
from lib.orders import Orders
from woocommerce import API

global ORDERID
wcapi = API(
    url="http://localhost:8000",
    consumer_key="ck_747561c1957b4d5e9c4ba174397365f9bdf43ab7",
    consumer_secret="cs_ae256b8de43dd771568cab572c8c135b11ff21f3",
    timeout=50
)


def test_create_order():
    response = Orders().create_order_with_coupon(wcapi)
    assert response.ok
    global ORDERID
    ORDERID = response.json()['id']
    orderEmail = response.json()['billing']['email']
    assert orderEmail == Orders(
    ).order['billing']['email'], 'Verify the order was created by checking the email'


def test_delete_order():
    response = Orders().delete_order(wcapi, ORDERID)
    assert response.ok
