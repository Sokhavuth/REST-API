#models/categorydb/getdb.py
import setConnection

def call(amount):
    cursor, connection = setConnection.call()

    cursor.execute("SELECT * FROM category ORDER BY datetime(datetime) DESC LIMIT ?", (amount,))
    categories = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM category")
    count = cursor.fetchone()
    
    cursor.close()

    return categories, count[0]