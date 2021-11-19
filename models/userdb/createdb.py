#models/userdb/createdb.py
import setConnection

def call(name, thumb, datetime, email, password, content, id, role, entries, edit):
    cursor, connection = setConnection.call()

    if not edit:
        sql = "INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (name, thumb, datetime, email, password, content, id, role, entries))
    else:
        sql = """UPDATE post SET
            title = ?,
            thumb = ?,
            datetime = ?,
            content = ?,
            category = ?,
            entries = ?
            
            WHERE id = ? """

        cursor.execute(sql, (title, thumb, datetime, content, category, entries, id))

    connection.commit()
    cursor.close()