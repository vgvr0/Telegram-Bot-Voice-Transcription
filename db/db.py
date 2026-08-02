import sqlite3

from datetime import datetime



class Users:
    def __init__(self, file='db/users.db'):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()




    def init_db(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Users (
                ID INTEGER PRIMARY KEY,
                name TEXT,
                username TEXT,
                count_transcript INTEGER,
                registrate DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_message DATETIME
            )
            '''
        )



    def manage_user(self, user_id, name, username):
        now = datetime.now().astimezone()


        self.cursor.execute('SELECT ID FROM Users WHERE ID = ?', (user_id,))
        user = self.cursor.fetchone()


        if user is None:
            self.cursor.execute('''INSERT INTO Users (ID, name, username, count_transcript, registrate, last_message) VALUES (?, ?, ?, ?, ?, ?) ''', (user_id, name, username, 0, now, now))


        else:
            self.cursor.execute('''UPDATE Users SET name = ?, username = ?, last_message = ? WHERE ID = ? ''', (name, username, now, user_id))
            self.cursor.execute('UPDATE Users SET count_transcript = count_transcript + 1 WHERE ID = ?', (user_id,))


        self.conn.commit()
        self.conn.close()



