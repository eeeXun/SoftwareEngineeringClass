import sqlite3

DBNAME = "test.db"


class Item:
    @staticmethod
    def add_item(name, amount):
        with sqlite3.connect(DBNAME) as conn:
            stmt = "INSERT INTO items (name, amount) VALUES (?, ?);"
            conn.execute(stmt, [name, amount])
            conn.commit()

    @staticmethod
    def get_all_item():
        """
        return (name, amount)
        """
        with sqlite3.connect(DBNAME) as conn:
            stmt = "SELECT name, amount FROM items;"
            data = conn.execute(stmt).fetchall()
            return data
