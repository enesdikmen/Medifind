from passlib.hash import pbkdf2_sha256 as hasher


def get_pharmacy_data(cursor, pharmacy_username):
    cursor.execute("SELECT pharmacy_id, pharmacy_name, city_name, pharmacy_address FROM pharmacy WHERE pharmacy_username = %s;",(pharmacy_username, ))
    pharmacy_data = cursor.fetchone()
    if not len(pharmacy_data):
        return False, {"error": f"Pharmacy with username '{pharmacy_username}' doesn't exists."}

    pharmacy_id, pharmacy_name, city_name, pharmacy_address = pharmacy_data
    cursor.execute("SELECT medicine_name, medicine_count FROM stock WHERE pharmacy_id = %s;",(pharmacy_id, ))
    stock_data = cursor.fetchall()
    stock_list = []
    for stock in stock_data:
        stock_list.append({"medicine_name": stock[0], "medicine_count": stock[1]})
    # print(pharmacy_data)
    # print(stock_data)

    return True, {"pharmacy_id": pharmacy_id, 
    "pharmacy_name": pharmacy_name, 
    "city_name": city_name, 
    "pharmacy_address":pharmacy_address, 
    "stock":stock_list}



def get_pharmacy_data_all(cursor):
    cursor.execute("SELECT pharmacy_id, pharmacy_username, pharmacy_name, city_name, pharmacy_address FROM pharmacy;")
    pharmacy_datas = cursor.fetchall()
    if not len(pharmacy_datas):
        return []

    pharmacy_data_list = []
    for pharmacy_data in pharmacy_datas:
        pharmacy_id, pharmacy_username, pharmacy_name, city_name, pharmacy_address = pharmacy_data
        cursor.execute("SELECT medicine_name, medicine_count FROM stock WHERE pharmacy_id = %s;",(pharmacy_id, ))
        stock_data = cursor.fetchall()
        stock_list = []
        for stock in stock_data:
            stock_list.append({"medicine_name": stock[0], "medicine_count": stock[1]})

        pharmacy_data_list.append({"pharmacy_id": pharmacy_id, 
        "pharmacy_name": pharmacy_name, 
        "pharmacy_username": pharmacy_username, 
        "city_name": city_name, 
        "pharmacy_address":pharmacy_address, 
        "stock":stock_list})

    return pharmacy_data_list


def add_pharmacy(cursor, pharmacy_username, pharmacy_name, pharmacy_password, city_name, pharmacy_address):
    cursor.execute("SELECT EXISTS(SELECT * FROM pharmacy WHERE pharmacy_username = %s);",(pharmacy_username, ))
    username_exists = cursor.fetchone()[0]

    if username_exists:
        return False, {"error": f"Pharmacy with username '{pharmacy_username}' already exists."}

    #hashing password with sha256 before storing in DB
    hashed_password = hasher.hash(pharmacy_password)

    cursor.execute("INSERT INTO pharmacy (pharmacy_username, pharmacy_name, pharmacy_password, city_name, pharmacy_address) VALUES (%s, %s, %s, %s, %s);",
    (pharmacy_username, pharmacy_name, hashed_password, city_name, pharmacy_address))

    pharmacy_id = cursor.lastrowid
    return True, {"detail": "Pharmacy successfully added.", "pharmacy_id":pharmacy_id}



def update_pharmacy(cursor, pharmacy_id, pharmacy_username, pharmacy_name, pharmacy_password, city_name, pharmacy_address):
    cursor.execute("SELECT EXISTS(SELECT * FROM pharmacy WHERE pharmacy_username = %s and pharmacy_id != %s);",(pharmacy_username, pharmacy_id,))
    username_exists = cursor.fetchone()[0]

    if username_exists:
        return False, {"error": f"Another pharmacy with username '{pharmacy_username}' already exists."}

    #when password is provided
    print("password: ", pharmacy_password)
    if pharmacy_password and type(pharmacy_password) == str and len(pharmacy_password) >= 1:
        hashed_password = hasher.hash(pharmacy_password)
        cursor.execute("UPDATE pharmacy SET pharmacy_username=%s, pharmacy_name=%s, pharmacy_password=%s, city_name=%s, pharmacy_address=%s WHERE pharmacy_id=%s;",
        (pharmacy_username, pharmacy_name, hashed_password, city_name, pharmacy_address, pharmacy_id))
    else:
        cursor.execute("UPDATE pharmacy SET pharmacy_username=%s, pharmacy_name=%s, city_name=%s, pharmacy_address=%s WHERE pharmacy_id=%s;",
        (pharmacy_username, pharmacy_name, city_name, pharmacy_address, pharmacy_id))


    return True, {"detail": "Pharmacy data successfully updated."}

def delete_pharmacy(cursor, pharmacy_id):
    cursor.execute("DELETE FROM pharmacy WHERE pharmacy_id = %s;", (pharmacy_id, ))
        # return False, {"error": f"Another pharmacy with username '{pharmacy_username}' already exists."}
    return True, {"detail": "Pharmacy successfully deleted."}


def get_stock(cursor, pharmacy_id, medicine_name):
    cursor.execute("SELECT EXISTS(SELECT * FROM stock WHERE pharmacy_id = %s and medicine_name=%s);",(pharmacy_id, medicine_name, ))
    stock_exists = cursor.fetchone()[0]

    if not stock_exists:
        return False, {"error": f"Stock record with pharmacy_id: '{pharmacy_id}' and medicine_name: '{medicine_name}' doesn't exists."}

    cursor.execute("SELECT medicine_count FROM stock WHERE pharmacy_id = %s and medicine_name=%s;",(pharmacy_id, medicine_name))
    medicine_count = cursor.fetchone()[0]

    return True, {"medicine_count": medicine_count}

def get_stocks(cursor, pharmacy_id):

    stock_list = []
    cursor.execute("SELECT pharmacy_id, medicine_name, medicine_count FROM stock WHERE pharmacy_id=%s;",(pharmacy_id, ))
    stocks = cursor.fetchall()
    for stock in stocks:
        stock_list.append({"pharmacy_id": stock[0], "medicine_name": stock[1], "medicine_count": stock[2]})

    return True, {"stocks": stock_list}

def add_stock(cursor, pharmacy_id, medicine_name, medicine_count):
   
    cursor.execute("SELECT EXISTS(SELECT * FROM stock WHERE pharmacy_id = %s and medicine_name=%s);",(pharmacy_id, medicine_name, ))
    stock_exists = cursor.fetchone()[0]

    if stock_exists:
        return False, {"error": f"Stock record with pharmacy_id: '{pharmacy_id}' and medicine_name: '{medicine_name}' already exists."}

    cursor.execute("INSERT INTO stock (pharmacy_id, medicine_name, medicine_count) VALUES (%s, %s, %s);",
    (pharmacy_id, medicine_name, medicine_count, ))

    return True, {"detail": "Stock successfully added."}



def update_stock(cursor, pharmacy_id, medicine_name, medicine_count):
    cursor.execute("SELECT EXISTS(SELECT * FROM stock WHERE pharmacy_id = %s and medicine_name=%s);",(pharmacy_id, medicine_name, ))
    stock_exists = cursor.fetchone()[0]

    if not stock_exists:
        return False, {"error": f"Stock record with pharmacy_id: '{pharmacy_id}' and medicine_name: '{medicine_name}' doesn't exists. So can't update."}

    cursor.execute("UPDATE stock SET medicine_count=%s WHERE pharmacy_id=%s and medicine_name=%s;",
    (medicine_count, pharmacy_id, medicine_name))


    return True, {"detail": "Stock data successfully updated."}

def delete_stock(cursor, pharmacy_id, medicine_name):
    cursor.execute("DELETE FROM stock WHERE pharmacy_id = %s and medicine_name=%s;", (pharmacy_id, medicine_name))
    return True, {"detail": "Stock data successfully deleted."}


def search_stock(cursor, medicine_name, city_name):

    cursor.execute("""
    SELECT s.medicine_name, s.pharmacy_id, p.city_name, p.pharmacy_name, p.pharmacy_address
    FROM stock s
    JOIN pharmacy p ON s.pharmacy_id = p.pharmacy_id
    WHERE s.medicine_name = %s
    """,(medicine_name, ))
    
    medicines = cursor.fetchall()
    if not medicines:
        return False, {"error": f"Medicine with medicine_name: '{medicine_name}' not found."}
    medicine_list = []
    city_names = []
    for medicine in medicines:
        if medicine[2] not in city_names: city_names.append(medicine[2])

        if medicine[2] == city_name:
            medicine_list.append({"medicine_name": medicine[0], "pharmacy_id": medicine[1], "city_name": medicine[2],
            "pharmacy_name": medicine[3], "pharmacy_address": medicine[4]})

    if len(medicine_list) > 0:
        return True, {"medicines": medicine_list}

    else:


        return True, {"detail": "Medicine not found within city.", "cities": city_names}

    
    
    
    