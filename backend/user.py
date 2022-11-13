import sqlite3

DBNAME = "test.db"


class User:
    @staticmethod
    def login(username, pwd):
        """
        success return 1
        wrong password return 0
        not register return -1
        """
        db_file = "test.db"
        with sqlite3.connect(db_file) as conn:
            stmt = "SELECT id, pwd FROM users WHERE username == '{}'".format(
                username
            )
            cursor = conn.cursor()
            cursor.execute(stmt)
            d = cursor.fetchone()

            if not d:
                return -1
            else:
                if d[1] == pwd:
                    return 0
                else:
                    return 0

    @staticmethod
    def register(username, pwd):
        """
        success return 1
        failed return 0
        """
        with sqlite3.connect(DBNAME) as conn:
            stmt = "INSERT INTO users (username, pwd) VALUES (?, ?);"
            conn.execute(stmt, [username, pwd])
            conn.commit()
        return 1
