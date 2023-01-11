import logging
import azure.functions as func
import mysql.connector
import azure.functions as func
from utils.utils import db_config
from utils.db_utils import get_pharmacy_data, get_pharmacy_data_all

import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        conn = mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:

        return func.HttpResponse(body=str(err), status_code=500)
    try:

        cursor = conn.cursor()
        pharmacy_data = get_pharmacy_data_all(cursor)


        cursor.close()
        conn.close()

        return func.HttpResponse(body=json.dumps({
            "pharmacy_data": pharmacy_data,
            }), status_code=200)
    
    except Exception as ex:
        return func.HttpResponse(body =json.dumps({"Exception": str(ex)}), status_code=500)