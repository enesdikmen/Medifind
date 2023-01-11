import logging, json
import mysql.connector
import azure.functions as func
from utils.utils import db_config
from utils.db_utils import delete_stock
import traceback


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        conn = mysql.connector.connect(**db_config)

        cursor = conn.cursor()
        req_body = req.get_json()
        
        if 'medicine_name' in req_body and req_body['medicine_name']:
            is_success, detail = delete_stock(cursor, req_body['pharmacy_id'], req_body['medicine_name'])
        else:
            return func.HttpResponse(body =json.dumps({"error": "No valid 'pharmacy_id' or 'medicine_name' provided."}), status_code=400)

        print(req_body['pharmacy_id'])
        print(req_body['medicine_name'])

        conn.commit()
        cursor.close()
        conn.close()

        if not is_success:
            return func.HttpResponse(body =json.dumps(detail), status_code=400)

        return func.HttpResponse(body = json.dumps(detail), status_code=200)
    
    except Exception as ex:
        traceback.print_exc()
        return func.HttpResponse(body =json.dumps({"exception": str(ex)}), status_code=500)
    
    