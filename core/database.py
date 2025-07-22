# Se MariaDB
import mariadb

# Se Postgres
# import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="sua_senha",
    host="localhost",
    port=5432,
    database="tribunal"
)

class Database:
    def __init__(self):
        # Se MariaDB
        self.connection = mariadb.connect(
            host="localhost",
            user="root",
            password="root",
            database="fidelity"
        )

        # Se Postgres
        # self.connection = psycopg2.connect(
        #     user="postgres",
        #     password="sua_senha",
        #     host="localhost",
        #     port=5432,
        #     database="fidelity"
        # )

        self.cursor = self.connection.cursor()

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()