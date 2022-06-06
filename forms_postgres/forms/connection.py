import psycopg2
import psycopg2 as db


HOST_NAME = 'localhost'
USERNAME = 'user_form'
PASSWORD = 'userpassword'
DB_NAME = 'form_db'


def save_to_db(data):
    create_table_query = '''CREATE TABLE IF NOT EXISTS form_table
    (id serial PRIMARY KEY, data jsonb);
    '''
    insert_query = '''INSERT INTO form_table ("data") VALUES (%s);'''
    try:
        conn = db.connect(
            host=HOST_NAME,
            user=USERNAME,
            password=PASSWORD,
            dbname=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        cursor.execute(insert_query, (data,))
        conn.commit()
        print(f'Data - with data {data} - is added')
    except (Exception, psycopg2.Error) as error:

        print(
            f'Failed to insert {data}.',
            error
        )
    finally:
        if conn:
            cursor.close()
            conn.close()
            print('Connection closed')
