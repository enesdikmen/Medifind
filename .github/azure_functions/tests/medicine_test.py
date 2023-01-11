import unittest, json
import azure.functions as func
import json
 
from get_medicine_names import main as get_medicine_names
from add_stock import main as add_stock
from update_stock import main as update_stock
from delete_stock import main as delete_stock
from get_stock import main as get_stock
from get_stocks import main as get_stocks
from search_medicine import main as search_medicine

class TestMedicine(unittest.TestCase):

  # Note how the test case starts with test_
  def test_get_medicine_names(self):
    # Arrange
    request = func.HttpRequest(
    method='GET',
    url='',
    params=None,
    body=None)

    response = get_medicine_names(request)
    # Assert we have a success code
    assert response.status_code == 200


  def test_add_stock(self):
    # Arrange
    request = func.HttpRequest(
    method='POST',
    url='',
    params=None,
    body=json.dumps({
        "pharmacy_id": 12,
        "medicine_name": "AFINITOR2",
        "medicine_count": 13
        }).encode('utf8'))

    response = add_stock(request)
    # Assert we have a success code
    assert response.status_code == 200

  def test_add_stock_exception(self):
    # Arrange
    request = func.HttpRequest(
    method='POST',
    url='',
    params=None,
    body=json.dumps({
        "medicine_count": 13
        }).encode('utf8'))

    response = add_stock(request)
    # Assert we have a success code
    assert response.status_code == 500
    

  def test_update_stock(self):
    # Arrange
    request = func.HttpRequest(
    method='POST',
    url='',
    params=None,
    body=json.dumps({
        "pharmacy_id": 12,
        "medicine_name": "Parol",
        "medicine_count": 88
        }).encode('utf8'))

    response = update_stock(request)
    # Assert we have a success code
    assert response.status_code == 200


  def test_update_stock_exception(self):
    # Arrange
    request = func.HttpRequest(
    method='POST',
    url='',
    params=None,
    body=json.dumps({
        "medicine_count": 88
        }).encode('utf8'))

    response = update_stock(request)
    # Assert we have a success code
    assert response.status_code == 500

  def test_delete_stock(self):
  # Arrange
    request = func.HttpRequest(
    method='POST',
    url='',
    params=None,
    body=json.dumps({
      "pharmacy_id": 12,
      "medicine_name": "AFINITOR2"
      }).encode('utf8'))

    response = delete_stock(request)
    # Assert we have a success code
    assert response.status_code == 200


  def test_delete_stock_exception(self):
  # Arrange
    request = func.HttpRequest(
    method='POST',
    url='',
    params=None,
    body=json.dumps({
      "medicine_name": "Parol"
      }).encode('utf8'))

    response = delete_stock(request)
    # Assert we have a success code
    assert response.status_code == 500

  def test_get_stock(self):
  # Arrange
    request = func.HttpRequest(
    method='POST',
    url='',
    params=None,
    body=json.dumps({
        "pharmacy_id": 12,
        "medicine_name": "Parol"
        }).encode('utf8'))

    response = get_stock(request)
    # Assert we have a success code
    assert response.status_code == 200



  def test_get_stock_exception(self):
    # Arrange
      request = func.HttpRequest(
      method='POST',
      url='',
      params=None,
      body=json.dumps({
          }).encode('utf8'))

      response = get_stock(request)
      # Assert we have a success code
      assert response.status_code == 500

  def test_get_stocks(self):
    # Arrange
    request = func.HttpRequest(
    method='POST',
    url='',
    params=None,
    body=json.dumps({
      "pharmacy_id": 12
    }).encode('utf8'))

    response = get_stocks(request)
    # Assert we have a success code
    assert response.status_code == 200

  def test_get_stocks_exception(self):
    # Arrange
    request = func.HttpRequest(
    method='POST',
    url='',
    params=None,
    body=json.dumps({
    }).encode('utf8'))

    response = get_stocks(request)
    # Assert we have a success code
    assert response.status_code == 500


  def test_search_medicine(self):
  # Arrange
    request = func.HttpRequest(
    method='POST',
    url='',
    params=None,
    body=json.dumps({
        "medicine_name": "Parol",
        "city_name": "İstanbul"      
        }).encode('utf8'))

    response = search_medicine(request)
    # Assert we have a success code
    assert response.status_code == 200

  def test_search_medicine_exception(self):
  # Arrange
    request = func.HttpRequest(
    method='POST',
    url='',
    params=None,
    body=json.dumps({
        }).encode('utf8'))

    response = search_medicine(request)
    # Assert we have a success code
    assert response.status_code == 500
