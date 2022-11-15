import sqlite3

from flask import session

DBNAME = "test.db"


class User:
    @staticmethod
    def login(username, pwd):
        """
        success return 1
        wrong password return 0
        not register return -1
        """
        with sqlite3.connect(DBNAME) as conn:
            stmt = "SELECT id, pwd FROM users WHERE username == '{}'".format(
                username
            )
            cursor = conn.cursor()
            cursor.execute(stmt)
            data = cursor.fetchone()

            if not data:
                return -1
            else:
                if data[1] == pwd:
                    session["id"] = data[0]
                    return 1
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

    @staticmethod
    def get_username(uid):
        with sqlite3.connect(DBNAME) as conn:
            stmt = "SELECT username FROM users WHERE id == (?)"
            username = conn.execute(stmt, [uid]).fetchone()[0]
            return username
