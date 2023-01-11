import logging
import azure.functions as func
import mysql.connector
import azure.functions as func
from utils.utils import db_config
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        conn = mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:

        return func.HttpResponse(body=str(err), status_code=500)
    try:

        cursor = conn.cursor()

        cursor.execute("SELECT DISTINCT medicine_name FROM stock;")
        medicines_names = cursor.fetchall()
        medicine_names_list = []

        for name in medicines_names:
            medicine_names_list.append(name[0])
        


        conn.commit()
        cursor.close()
        conn.close()

        return func.HttpResponse(body=json.dumps({
            "medicines_names": medicine_names_list,

            }), status_code=200)
    
    except Exception as ex:
        return func.HttpResponse(body =json.dumps({"Exception": str(ex)}), status_code=500)