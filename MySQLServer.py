#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server (change credentials if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Dohardthings1.1"  # Change to your MySQL password or leave "" if none
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()

