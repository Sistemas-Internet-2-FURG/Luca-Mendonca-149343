import psycopg2
import sys
import os
from models.dealer import Dealer

CONTAINER_HOST = os.environ.get('HOST')

if CONTAINER_HOST:
    HOST = CONTAINER_HOST


def select_dealers():
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()

    cur.execute('''SELECT * FROM dealer''')

    data = cur.fetchall()

    cur.close()
    conn.close()

    dealer = []
    for c in data:
        dealer.append(Dealer(c[0], c[1], c[2], c[3]))
        
    return dealer

def getDealerNameById(id:int):
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()

    try:
        cur.execute(f'''SELECT name FROM dealer WHERE id={id}''')
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