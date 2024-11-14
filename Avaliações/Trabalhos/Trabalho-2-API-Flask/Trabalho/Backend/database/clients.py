import psycopg2
import sys
import os
from models.client import Client

CONTAINER_HOST = os.environ.get('HOST')

if CONTAINER_HOST:
    HOST = CONTAINER_HOST

def insert_client(name:str, email:str, phone:str):
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()  

    try:
        cur.execute('''INSERT INTO client (name, email, phone) VALUES (%s, %s, %s)''', (str(name), str(email), str(phone)))
    except:
        cur.close()
        conn.close()
        return False

    conn.commit()

    cur.close()
    conn.close()

    return True

def update_client(name:str, email:str, phone:str):
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()  
    
    try:
        cur.execute('''UPDATE client SET email=%s, phone=%s WHERE name=%s''', (str(email), str(phone), str(name)))
    except:
        cur.close()
        conn.close()
        return False

    conn.commit()

    cur.close()
    conn.close()

    return True

def select_clients():
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()    

    cur.execute('''SELECT * FROM client''')

    data = cur.fetchall()

    cur.close()
    conn.close()

    clients = []
    for c in data:
        cli_tmp = Client(c[0], c[1], c[2], c[3])
        clients.append(cli_tmp.json_me())
        
    return clients

def getClientIdByName(name:str):
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()

    try:
        cur.execute(f'''SELECT id FROM client WHERE name='{name}' ''')
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

def getClientNameById(id:int):
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()

    try:
        cur.execute(f'''SELECT name FROM client WHERE id={id}''')
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