import psycopg2
import time
import allure
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
    drop_table(cursor, conn)
    cursor.close()
    conn.close()


@allure.feature("Connection to DB")
@allure.title("Test Insert, Update, Select - User")
def test_data_insertion(test_database_connection):
    time.sleep(1)
    conn = test_database_connection
    cursor = conn.cursor()
    insert_user(cursor, conn, 1, "Vitalii")
    update_user(cursor, conn, 1, "Vasia")
    result = select_user_by_id(cursor, 1)
    verify_user_name(result[1], "Vasia")


@allure.step("Insert User")
def insert_user(cursor, conn, id, user_name):
    cursor.execute(f"INSERT INTO users (UserId, FirstName) VALUES ({id}, '{user_name}')")
    conn.commit()


@allure.step("Update User")
def update_user(cursor, conn, id, user_name):
    cursor.execute(f"UPDATE users SET FirstName='{user_name}' WHERE UserId={id}")
    conn.commit()


@allure.step("Select User")
def select_user_by_id(cursor, id):
    cursor.execute(f"SELECT * FROM users WHERE UserId={id}")
    return cursor.fetchone()


@allure.step("Verify User FirstName")
def verify_user_name(actual_name, expected_name):
    assert actual_name == expected_name


@allure.step("Drop Table Users")
def drop_table(cursor, conn):
    cursor.execute("""DROP TABLE users;""")
    conn.commit()
