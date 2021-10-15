#models/categorydb/createdb.py
import setConnection

def call(name, link, datetime, id):
    cursor, connection = setConnection.call()

    cursor.execute("INSERT INTO category VALUES(?, ?, ?, ?)", (name, link, datetime, id))

    connection.commit()
    cursor.close()