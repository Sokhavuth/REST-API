#models/categorydb/createdb.py
import setConnection

def call(name, link, datetime):
    cursor, connection = setConnection.call()

    cursor.execute("INSERT INTO category VALUES(?, ?, ?)", (name, link, datetime))

    connection.commit()
    cursor.close()