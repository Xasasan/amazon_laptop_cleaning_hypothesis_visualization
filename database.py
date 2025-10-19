import psycopg2 as d
def connect():
    data = d.connect(
        host='localhost',
        dbname='postgres',
        user='postgres',
        password='55544423'
    )
    return data

def save_users(tg_id, name, age, phone):
    db = connect()
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    tg_id BIGINT UNIQUE,
    name VARCHAR,
    phone VARCHAR)
    ''')
    cursor.execute('''
    INSERT INTO users(tg_id, name, age, phone)
    VALUES (%s, %s, %s, %s''', (tg_id, name, age, phone))
    db.commit()
    db.close()
