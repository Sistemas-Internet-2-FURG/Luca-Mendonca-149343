import psycopg2
import sys
import os
from models.car import Car

CONTAINER_HOST = os.environ.get('HOST')

if CONTAINER_HOST:
    HOST = CONTAINER_HOST

def select_cars():
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()

    cur.execute('''SELECT * FROM car''')

    data = cur.fetchall()

    cur.close()
    conn.close()

    cars = []
    for c in data:
        cars.append(Car(c[0], c[1], c[2]))
        
    return cars

def getCarIdByName(name:str):
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()

    try:
        cur.execute(f'''SELECT id FROM car WHERE name='{name}' ''')
    except:
        cur.close()
        conn.close()
        return False

    data = cur.fetchall()
    
    cur.close()
    conn.close()
    if data == []:
        return False

    return data[0][0]

def getCarNameById(id:int):
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()

    try:
        cur.execute(f'''SELECT name FROM car WHERE id={id}''')
    except:
        cur.close()
        conn.close()
        return False

    data = cur.fetchall()
    
    cur.close()
    conn.close()
    if data == []:
        return False

    return data[0][0]