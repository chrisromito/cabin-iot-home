import sqlite3

from settings import DB_PATH


connection = sqlite3.connect(DB_PATH)


def get_connection():
    global connection
    return connection
