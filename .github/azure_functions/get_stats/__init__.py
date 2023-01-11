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
        cursor.execute("SELECT SUM(medicine_count) FROM stock;")
        result = cursor.fetchone()
        print(result)
        
        if result: 
            medicine_count = int(result[0])
        else:
            medicine_count = 0

        cursor.execute("SELECT COUNT(DISTINCT city_name) FROM pharmacy;")
        result = cursor.fetchone()
        print(result)
        
        if result: 
            city_count = result[0]
        else:
            city_count = 0

        cursor.execute("SELECT COUNT(DISTINCT medicine_name) FROM stock;")
        result = cursor.fetchone()
        print(result)
        
        if result: 
            distinct_medicine_count = result[0]
        else:
            distinct_medicine_count = 0


        cursor.execute("SELECT COUNT(*) FROM pharmacy;")
        result = cursor.fetchone()
        print(result)
        if result: 
            pharmacy_count = result[0]
        else:
            pharmacy_count = 0
            

        # cursor.execute("SELECT img_url, title, body, site_url, uuid FROM video WHERE video_id = %s;",(req_body['video_id'], ))
        # img_url, title, body, site_url, save_uuid = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return func.HttpResponse(body=json.dumps({
            "city_count": city_count,
            "pharmacy_count": pharmacy_count,
            "medicine_count": medicine_count,
            "distinct_medicine_count": distinct_medicine_count,

            }), status_code=200)
    
    except Exception as ex:
        return func.HttpResponse(body =json.dumps({"Exception": str(ex)}), status_code=500)