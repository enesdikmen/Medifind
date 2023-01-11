import logging, json
import mysql.connector
import azure.functions as func
from utils.utils import db_config
from utils.db_utils import get_stocks
import traceback



def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        conn = mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:

        return func.HttpResponse(body=str(err), status_code=500)
    try:
        req_body = req.get_json()

        cursor = conn.cursor()
        is_success, detail = get_stocks(cursor, req_body['pharmacy_id'])
        print("asd")
        print(req_body['pharmacy_id'])
        if not is_success:
            return func.HttpResponse(body =json.dumps(detail), status_code=400)

        return func.HttpResponse(body = json.dumps(detail), status_code=200)
    
    except Exception as ex:
        traceback.print_exc()
        return func.HttpResponse(body =json.dumps({"exception": str(ex)}), status_code=500)
    
    