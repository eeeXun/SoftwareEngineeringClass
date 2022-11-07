import sqlite3


class User:
    @staticmethod
    def login(username, pwd):
        """
        success return 1
        not register return 0
        wrong password return -1
        """
        db_file = "test.db"
        with sqlite3.connect(db_file) as conn:
            stmt = "SELECT id, pwd FROM users WHERE username == {}".format(
                username
            )
            cursor = conn.cursor()
            cursor.execute(stmt)
            d = cursor.fetchone()

            if not d:
                return 0
            else:
                if d[1] == pwd:
                    return 1
                else:
                    return -1
