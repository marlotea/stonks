import mysql.connector
from ..config import DB_USERNAME, DB_PASSWORD


def get_connection():
    return mysql.connector.connect(
    host="localhost",
    user=DB_USERNAME,
    password=DB_PASSWORD
    )

def insert_stock_data(symbol, date, open_price, high_price, low_price, close_price, volume):
    conn = get_connection()
    cursor = conn.cursor()
    query = """INSERT INTO stock_data (symbol, date, open, high, low, close, volume) 
               VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (symbol, date, open_price, high_price, low_price, close_price, volume))
    conn.commit()
    cursor.close()
    conn.close()
    
def initialize_db():
    mycursor = get_connection().cursor()

    mycursor.execute("CREATE DATABASE stockdata_db")
    mycursor.execute("CREATE DATABASE recommendations_db")
