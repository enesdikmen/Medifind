import mysql.connector
from passlib.hash import pbkdf2_sha256 as hasher

db_config = {
    'host':'medifind.mysql.database.azure.com',
    'user':'medifind_admin',
    'password':'Softeng34',
    'database':'medifind_db',
    }

def authenticate_admin(cursor, admin_username, password):
    cursor.execute("SELECT admin_id, admin_password FROM admin WHERE admin_username = %s;",(admin_username, ))
    user_data = cursor.fetchone()
    if not user_data:
        return False, {"error": f"Admin user with username '{admin_username}' doesn't exists."}
    hashed_pasword = user_data[1]
    if hasher.verify(password, hashed_pasword):#true if password is correct
        return True, {"detail": "User credentials are valid", "admin_id": user_data[0]}
    else:
        return False, {"detail": "User credentials are not valid"}


def authenticate_pharmacy(cursor, pharmacy_username, password):
    cursor.execute("SELECT pharmacy_id, pharmacy_password FROM pharmacy WHERE pharmacy_username = %s;",(pharmacy_username, ))
    user_data = cursor.fetchone()
    if not user_data:
        return False, {"error": f"Pharmacy user with username '{pharmacy_username}' doesn't exists."}

    hashed_pasword = user_data[1]
    if hasher.verify(password, hashed_pasword):#true if password is correct
        return True, {"detail": "User credentials are valid", "pharmacy_id": user_data[0]}
    else:
        return False, {"detail": "User credentials are not valid"}




