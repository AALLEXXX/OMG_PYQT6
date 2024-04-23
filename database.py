import mysql.connector
from typing import List, Tuple
from datetime import datetime

config = {
    'user': 'root',
    'password': 'alxxlapP123!@',
    'host': 'localhost',
    'database': 'test_db',
    'raise_on_warnings': True
}

class Database:
    def __init__(self):
        self.connection = self.__get_connect_to_db()
        self.cursor = self.connection.cursor()

    def __get_connect_to_db(self):
        try:
            connection = mysql.connector.connect(**config)
            print("Подключение успешно!")
            return connection
        except mysql.connector.Error as err:
            print(f"Ошибка подключения: {err}")
            exit(1)

    def get_position(self) -> List[tuple]:
        self.cursor.execute("SELECT * from positions")
        rows = self.cursor.fetchall()
        return rows


    def reg_new_user(self, login, password, mail='', phone='') -> bool:
        date = datetime.now()
        self.cursor.execute("select check_password(%s)", (password, ))
        result = self.cursor.fetchone()[0]
        if result:
            try:
                self.cursor.execute("INSERT INTO users (login, hash_password, last_visit, mail, phone) VALUES (%s, sha2(%s, 256), %s, %s, %s)",
                                    (login, password, date, mail, phone))
                self.connection.commit()
                return True
            except Exception as e:
                print(e)
        return False

    def auth_user(self, login, password) -> Tuple[str, bool]:
        result = ''
        is_valid = False
        result = self.cursor.callproc('auth_user', (login, password, result, is_valid))
        return (result[2], result[3])

# a = Database()
# a.auth_user('alex','admin123')

# a.cursor.callproc("GetPos", )
# result = a.cursor.stored_results()
# print(next(result).fetchall())