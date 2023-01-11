import azure.functions as func
import mysql.connector
import azure.functions as func
from utils.utils import db_config
import json
from passlib.hash import pbkdf2_sha256 as hasher

def main(req: func.HttpRequest) -> func.HttpResponse:


    conn = mysql.connector.connect(**db_config)

    try:

        cursor = conn.cursor()
        req_body = req.get_json()
        
        cursor.execute("SELECT EXISTS(SELECT * FROM pharmacy WHERE pharmacy_id = %s);",(req_body['pharmacy_id'],))
        pharmacy_exists = cursor.fetchone()[0]

        if not pharmacy_exists:
            return func.HttpResponse(body =json.dumps({"error": f"Pharmacy with id: '{req_body['pharmacy_id']}' not found."}), status_code=400)
        
        hashed_password = hasher.hash(req_body['pharmacy_password'])

        cursor.execute("UPDATE pharmacy SET pharmacy_password=%s WHERE pharmacy_id=%s;",
        (hashed_password, req_body['pharmacy_id'], ))

        print(hashed_password)
        print(req_body['pharmacy_id'])
        
        conn.commit()
        cursor.close()
        conn.close()

        return func.HttpResponse(body=json.dumps({
            "detail": "Pharmacy password successfully updated.",
            }), status_code=200)
    
    except Exception as ex:
        return func.HttpResponse(body =json.dumps({"Exception": str(ex)}), status_code=500)