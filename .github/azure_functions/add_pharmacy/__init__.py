import logging, json
import mysql.connector
import azure.functions as func
from utils.utils import db_config
from utils.db_utils import add_pharmacy, update_pharmacy
import traceback



def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        conn = mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:

        return func.HttpResponse(body=str(err), status_code=500)
    try:

        cursor = conn.cursor()
        req_body = req.get_json()
        
        #if pharmacy_id comes, then it is update operation
        if 'pharmacy_id' in req_body and req_body['pharmacy_id'] and type(req_body['pharmacy_id']) == int:
            is_success, detail = update_pharmacy(cursor, req_body['pharmacy_id'], req_body['pharmacy_username'], req_body['pharmacy_name'],req_body['pharmacy_password'], req_body['city_name'], req_body['pharmacy_address'])
        #otherways it adds a new pharmacy record
        else:
            is_success, detail = add_pharmacy(cursor, req_body['pharmacy_username'], req_body['pharmacy_name'],req_body['pharmacy_password'], req_body['city_name'], req_body['pharmacy_address'])

        conn.commit()
        cursor.close()
        conn.close()

        if not is_success:
            return func.HttpResponse(body =json.dumps(detail), status_code=400)

        return func.HttpResponse(body = json.dumps(detail), status_code=200)
    
    except Exception as ex:
        traceback.print_exc()
        return func.HttpResponse(body =json.dumps({"exception": str(ex)}), status_code=500)
    
    