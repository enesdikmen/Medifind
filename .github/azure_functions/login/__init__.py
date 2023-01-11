import logging, json
import mysql.connector
import azure.functions as func
from utils.utils import db_config, authenticate_admin, authenticate_pharmacy
from utils.db_utils import get_pharmacy_data

from passlib.hash import pbkdf2_sha256 as hasher

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        conn = mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:

        return func.HttpResponse(body=str(err), status_code=500)
    try:

        cursor = conn.cursor()
        req_body = req.get_json()

        login_type = req_body['login_type'] 
        user_name = req_body['user_name']
        password = req_body['password']

        if login_type == 'admin':
            is_authenticated, detail = authenticate_admin(cursor, user_name, password)
            if is_authenticated:
                
                # pharmacy_data = get_pharmacy_data(cursor, pharmacy_username=user_name)
                cursor.close()
                conn.close()
                return func.HttpResponse(body =json.dumps(detail), status_code=200)
            else:
                cursor.close()
                conn.close()
                return func.HttpResponse(body =json.dumps(detail), status_code=400)

        elif login_type == 'pharmacy':

            is_authenticated, detail = authenticate_pharmacy(cursor, user_name, password)
            if is_authenticated:
                pharmacy_data = get_pharmacy_data(cursor, pharmacy_username=user_name)
                if pharmacy_data[0]:
                    detail['pharmacy_data'] = pharmacy_data[1]
                cursor.close()
                conn.close()
                return func.HttpResponse(body =json.dumps(detail), status_code=200)
            else:
                cursor.close()
                conn.close()
                return func.HttpResponse(body =json.dumps(detail), status_code=400)

        else:
            return func.HttpResponse(body =json.dumps({"error": "Invalid 'login_type'."}), status_code=400)

    except Exception as ex:
        return func.HttpResponse(body =json.dumps({"Exception": str(ex)}), status_code=500)
    
    