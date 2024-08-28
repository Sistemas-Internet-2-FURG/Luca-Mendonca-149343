import psycopg2
import os

CONTAINER_HOST = os.environ.get('HOST')

if CONTAINER_HOST:
    HOST = CONTAINER_HOST

def dealer_login(name:str, password:str):
    conn = psycopg2.connect(database="app", user="root", 
                        password="root", host=HOST, port="5432")

    cur = conn.cursor()

    try:
        cur.execute(f'''SELECT password FROM dealer WHERE name='{name}' ''')
    except:
        return False

    data = cur.fetchall()

    cur.close()
    conn.close()

    try:
        real_password = data[0][0]
    except:
        return False

    if password == str(real_password):
        return True
    
    return False