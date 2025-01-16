import psycopg2
import time

import pytest


@pytest.fixture()
def test_database_connection():
    print("Test 1")
    time.sleep(2)
    conn = psycopg2.connect(
        dbname="test_db",
        user="test_user",
        password="test_password",
        host="db",
        port="5432"
    )
    assert conn is not None
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users (
    UserId int,
    FirstName varchar(255));
    """)
    conn.commit()
    yield conn
    cursor.execute("""DROP TABLE users;""")
    conn.commit()
    cursor.close()
    conn.close()



def test_data_insertion(test_database_connection):
    time.sleep(1)
    conn = test_database_connection
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (UserId, FirstName) VALUES (1, 'Vitalii')")
    conn.commit()
    cursor.execute("UPDATE users SET FirstName='Vasia' WHERE UserId=1")
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE UserId=1")
    result = cursor.fetchone()
    assert result[1] == 'Vasia'
