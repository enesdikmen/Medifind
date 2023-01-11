import unittest
import json
import azure.functions as func
import json

from add_pharmacy import main as add_pharmacy
from update_pharmacy import main as update_pharmacy

from delete_pharmacy import main as delete_pharmacy
from get_pharmacies import main as get_pharmacies
from get_stats import main as get_stats
from login import main as login
from update_admin import main as update_admin


class TestMedicine(unittest.TestCase):

    # Note how the test case starts with test_
    def test_add_pharmacy(self):
        # Arrange
        request = func.HttpRequest(
            method='POST',
            url='',
            params=None,
            body=json.dumps({
                "pharmacy_username": "faruk.eczane12",
                "pharmacy_name": "Meci Eczanesi2",
                "pharmacy_password": "123456",
                "city_name": "İstanbul",
                "pharmacy_address": "Mecidiyeköy Mah3."
            }).encode('utf8'))

        response = add_pharmacy(request)
        # Assert we have a success code
        assert response.status_code == 200


    def test_add_pharmacy_update(self):
        # Arrange
        request = func.HttpRequest(
            method='POST',
            url='',
            params=None,
            body=json.dumps({
                "pharmacy_id": 20,
                "pharmacy_username": "faruk.eczane3",
                "pharmacy_name": "Meci Eczanesi2",
                "pharmacy_password": "123456",
                "city_name": "İstanbul",
                "pharmacy_address": "Mecidiyeköy Mah3."
            }).encode('utf8'))

        response = add_pharmacy(request)
        # Assert we have a success code
        assert response.status_code == 200

    def test_add_pharmacy_incorrect(self):
        # Arrange
        request = func.HttpRequest(
            method='POST',
            url='',
            params=None,
            body=json.dumps({
                "pharmacy_username": "eczane1",
                "pharmacy_name": "Meci Eczanesi2",
                "pharmacy_password": "123456",
                "city_name": "İstanbul",
                "pharmacy_address": "Mecidiyeköy Mah3."
            }).encode('utf8'))

        response = add_pharmacy(request)
        # Assert we have a success code
        assert response.status_code == 400

    def test_update_pharmacy(self):
        # Arrange
        request = func.HttpRequest(
            method='POST',
            url='',
            params=None,
            body=json.dumps({
                "pharmacy_id": 20,
                "pharmacy_password": "1234"
            }).encode('utf8'))

        response = update_pharmacy(request)
        # Assert we have a success code
        assert response.status_code == 200

    def test_delete_pharmacy(self):
        # Arrange
        request = func.HttpRequest(
            method='POST',
            url='',
            params=None,
            body=json.dumps({
                "pharmacy_id": 43
            }).encode('utf8'))

        response = delete_pharmacy(request)
        # Assert we have a success code
        assert response.status_code == 200

    
    def test_delete_pharmacy_incorrect(self):
        # Arrange
        request = func.HttpRequest(
            method='POST',
            url='',
            params=None,
            body=json.dumps({
                
              }).encode('utf8'))

        response = delete_pharmacy(request)
        # Assert we have a success code
        assert response.status_code == 400

    def test_get_pharmacies(self):
        # Arrange
        request = func.HttpRequest(
            method='GET',
            url='',
            params=None,
            body=None)

        response = get_pharmacies(request)
        # Assert we have a success code
        assert response.status_code == 200

    def test_get_stats(self):
        # Arrange
        request = func.HttpRequest(
            method='GET',
            url='',
            params=None,
            body=None)

        response = get_stats(request)
        # Assert we have a success code
        assert response.status_code == 200

    def test_login_pharmacy_correct(self):
        # Arrange
        request = func.HttpRequest(
            method='POST',
            url='',
            params=None,
            body=json.dumps({
                "login_type": "pharmacy",
                "user_name": "eczane1",
                "password": "eczane1"
            }).encode('utf8'))

        response = login(request)
        # Assert we have a success code
        assert response.status_code == 200


    def test_login_pharmacy_incorrect(self):
        # Arrange
        request = func.HttpRequest(
            method='POST',
            url='',
            params=None,
            body=json.dumps({
            "login_type": "pharmacy",
            "user_name": "eczane21211",
            "password": "eczane1"
            }).encode('utf8'))

        response = login(request)
        # Assert we have a success code
        assert response.status_code == 400

    def test_login_admin_correct(self):
    # Arrange
        request = func.HttpRequest(
            method='POST',
            url='',
            params=None,
            body=json.dumps({
                "login_type": "admin",
                "user_name": "admin1",
                "password": "admin1"
            }).encode('utf8'))

        response = login(request)
        # Assert we have a success code
        assert response.status_code == 200

    def test_login_admin_incorrect(self):
        request = func.HttpRequest(
            method='POST',
            url='',
            params=None,
            body=json.dumps({
                "login_type": "admin",
                "user_name": "faruk.eczane3",
                "password": "123456"
            }).encode('utf8'))

        response = login(request)
        # Assert we have a success code
        assert response.status_code == 400


    def test_update_admin(self):
        # Arrange
        request = func.HttpRequest(
            method='POST',
            url='',
            params=None,
            body=json.dumps({
                "admin_id": 12,
                "admin_password": "1234"
            }).encode('utf8'))

        response = update_admin(request)
        # Assert we have a success code
        assert response.status_code == 200
