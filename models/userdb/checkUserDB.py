#models/userdb/checkUserDB.py
from . import setConnection

def call(email, password):
    cursor, connection = setConnection.call()

    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    cursor.close()

    return user