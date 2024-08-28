import psycopg2
import sys
import os
from models.sale import Sale
from database.clients import getClientIdByName, getClientNameById
from database.cars import getCarIdByName, getCarNameById
from database.dealers import getDealerNameById

CONTAINER_HOST = os.environ.get('HOST')

if CONTAINER_HOST:
    HOST = CONTAINER_HOST
    
def select_sales():
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()

    cur.execute('''SELECT * FROM sale''')

    data = cur.fetchall()

    cur.close()
    conn.close()

    sales = []
    for c in data:
        client_name = getClientNameById(c[1])
        dealer_name = getDealerNameById(c[3])
        car_name = getCarNameById(c[2])
        sales.append(Sale(c[0], client_name, dealer_name, car_name, c[4]))
        
    return sales


def insert_sale(client:str, car:str, dealer_id:int, price:int):
    # Call functions for getting the client id by name and car id by name
    
    client_id = getClientIdByName(client)

    if client_id == False:
        return False
    
    car_id = getCarIdByName(car)

    if car_id == False:
        return False

    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()
    print(client_id, car_id, dealer_id, price, file=sys.stdout)
    try:
        cur.execute('''INSERT INTO sale (client_id, car_id, dealer_id, price) VALUES (%s, %s, %s, %s)''', (client_id, car_id, dealer_id, price))
    except:
        cur.close()
        conn.close()
        return False

    conn.commit()

    cur.close()
    conn.close()

    return True

def remove_sale(id:int):
    
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")
    
    cur = conn.cursor()
    try:
        cur.execute(f'''DELETE FROM sale WHERE id={id}''')
    except:
        return False

    conn.commit()

    cur.close()
    conn.close()

    return True