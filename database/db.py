import sqlite3
from pathlib import Path
from datetime import datetime


# resolve DB relative to this file, not the process cwd
_DEFAULT_DB_PATH = Path(__file__).resolve().parent / 'users.database'


class Users:
    def __init__(self, db_path=None):
        self.db_path = str(db_path) if db_path else str(_DEFAULT_DB_PATH)


    def get_connection(self):
        return sqlite3.connect(self.db_path)


    def init_db(self):
        try:
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
                        block INTEGER NOT NULL DEFAULT 0,
                        registrate DATETIME DEFAULT CURRENT_TIMESTAMP,
                        last_message DATETIME
                    )
                    '''
                )


                conn.commit()

        except Exception as e:
            print(e)


    def manage_user(self, user_id, name, username):
        try:
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

        except Exception as e:
            print(e)



    def set_language(self, user_id, language):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()



                cursor.execute('UPDATE Users SET language = ? WHERE user_id = ?', (language, user_id))


                conn.commit()

        except Exception as e:
            print(e)






    def get_language(self, user_id):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()


                cursor.execute('SELECT language FROM Users WHERE user_id = ?', (user_id, ))
                language = cursor.fetchone()


                return language[0]


        except Exception as e:
            print(e)


    def get_users(self):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()


                cursor.execute('SELECT * FROM Users')
                users = cursor.fetchall()


                print(users)
                return users


        except Exception as e:
            print(e)




    def get_all_users_id(self):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()

                cursor.execute('SELECT user_id FROM Users')
                users = cursor.fetchall()

                return users


        except Exception as e:
            print(e)


    def privacy_block(self, user_id):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()


                cursor.execute('SELECT block FROM Users WHERE user_id = ?', (user_id, ))
                block = cursor.fetchone()

                if block is None:
                    return False

                if block[0] == 1:
                    return True

        except Exception as e:
            print(e)



    def change_status_user(self, user_id):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()


                if self.privacy_block(user_id):
                    cursor.execute('UPDATE Users SET block = ? WHERE user_id = ?', (0, user_id))


                else:
                    cursor.execute('UPDATE Users SET block = ? WHERE user_id = ?', (1, user_id))


                conn.commit()

        except Exception as e:
            print(e)









if __name__ == '__main__':
    db = Users()
    db.get_users()