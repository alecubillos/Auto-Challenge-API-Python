import pytest
import requests
import json
from lib.products import Products
from woocommerce import API

global VERIFYID

wcapi = API(
    url="http://localhost:8000",
    consumer_key="ck_747561c1957b4d5e9c4ba174397365f9bdf43ab7",
    consumer_secret="cs_ae256b8de43dd771568cab572c8c135b11ff21f3",
    timeout=50
)


def test_create_product():
    response = Products().create_product(wcapi)
    assert response.ok


def test_product_created():
    response = Products().get_all_products(wcapi)
    for p in range(len(response.json())):

        productName = response.json()[p]['name']
        productID = response.json()[p]['id']
        if productName == Products().product['name']:
            retrieveProduct = Products().get_product(wcapi, productID)
            verifyName = retrieveProduct.json()['name']
            global VERIFYID
            VERIFYID = retrieveProduct.json()['id']
            assert verifyName == Products(
            ).product['name'], 'Verify the product was created'


def test_delete_product():
    response = Products().delete_product(wcapi, VERIFYID)
    assert response.ok
