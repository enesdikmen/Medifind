import azure.functions as func
import mysql.connector
import azure.functions as func
from utils.utils import db_config
import json
from passlib.hash import pbkdf2_sha256 as hasher

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        conn = mysql.connector.connect(**db_config)

        cursor = conn.cursor()
        req_body = req.get_json()
        
        cursor.execute("SELECT EXISTS(SELECT * FROM admin WHERE admin_id = %s);",(req_body['admin_id'],))
        admin_exists = cursor.fetchone()[0]
        print(req_body['admin_id'])
        if not admin_exists:
            return func.HttpResponse(body =json.dumps({"error": f"Admin with id: '{req_body['admin_id']}' not found."}), status_code=400)
        
        hashed_password = hasher.hash(req_body['admin_password'])

        cursor.execute("UPDATE admin SET admin_password=%s WHERE admin_id=%s;",
        (hashed_password, req_body['admin_id'], ))

        print(hashed_password)
        conn.commit()
        cursor.close()
        conn.close()

        return func.HttpResponse(body=json.dumps({
            "detail": "Admin password successfully updated.",
            }), status_code=200)
    
    except Exception as ex:
        return func.HttpResponse(body =json.dumps({"Exception": str(ex)}), status_code=500)