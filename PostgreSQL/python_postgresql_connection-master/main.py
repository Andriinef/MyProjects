import psycopg2
from config import db_name, host, password, user

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host, user=user, password=password, database=db_name
    )
    connection.autocommit = True

    # # курсор для выполнения операций с базой данных
    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")

        print(f"Server version: {cursor.fetchone()}")

    # # создать новую таблицу
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL,
    #             nick_name varchar(50) NOT NULL);"""
    #     )

    #     # connection.commit()
    #     print("[INFO] Table created successfully")

    # # вставить данные в таблицу
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users (first_name, nick_name) VALUES
    #         ('Andrii', 'Andriinef');"""
    #     )

    #     print("[INFO] Data was succefully inserted")

    # # получить данные из таблицы
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT nick_name FROM users WHERE first_name = 'Danil';"""
    #         """SELECT nick_name FROM users WHERE first_name = 'Andrii';"""
    #     )
    #
    #     print(cursor.fetchone())

    # # удалить таблицу
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )

    #     print("[INFO] Table was deleted")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
