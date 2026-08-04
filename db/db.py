import sqlite3
from pathlib import Path
from datetime import datetime


# resolve DB relative to this file, not the process cwd
_DEFAULT_DB_PATH = Path(__file__).resolve().parent / 'users.db'


class Users:
    def __init__(self, db_path=None):
        self.db_path = str(db_path) if db_path else str(_DEFAULT_DB_PATH)


    def get_connection(self):
        return sqlite3.connect(self.db_path)


    def init_db(self):


        with self.get_connection() as conn:
            cursor = conn.cursor()



            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS Users (
                    user_id INTEGER PRIMARY KEY,
                    name TEXT,
                    username TEXT,
                    language TEXT,
                    count_transcript INTEGER,
                    registrate DATETIME DEFAULT CURRENT_TIMESTAMP,
                    last_message DATETIME
                )
                '''
            )


            conn.commit()


    def manage_user(self, user_id, name, username):
        now = datetime.now().astimezone()

        with self.get_connection() as conn:
            cursor = conn.cursor()


            cursor.execute('SELECT user_id FROM Users WHERE user_id = ?', (user_id,))
            user = cursor.fetchone()


            if user is None:
                cursor.execute(
                    '''INSERT INTO Users (user_id, name, username, count_transcript, registrate, last_message)
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (user_id, name, username, 0, now, now)
                )


            else:
                cursor.execute('''UPDATE Users SET name = ?, username = ?, last_message = ? WHERE user_id = ? ''', (name, username, now, user_id))
                cursor.execute('UPDATE Users SET count_transcript = count_transcript + 1 WHERE user_id = ?', (user_id,))


            conn.commit()



    def set_language(self, user_id, language):
        with self.get_connection() as conn:
            cursor = conn.cursor()



            cursor.execute('UPDATE Users SET language = ? WHERE user_id = ?', (language, user_id))


            conn.commit()






    def get_language(self, user_id):
        with self.get_connection() as conn:
            cursor = conn.cursor()


            cursor.execute('SELECT language FROM Users WHERE user_id = ?', (user_id, ))
            language = cursor.fetchone()


            return language[0]


    def get_users(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()


            cursor.execute('SELECT * FROM Users')
            users = cursor.fetchall()


            print(users)
            return users




    def get_all_users_id(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute('SELECT user_id FROM Users')
            users = cursor.fetchall()

            return users


if __name__ == '__main__':
    db = Users()
    db.get_users()