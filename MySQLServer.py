#!/usr/bin/env python3
import mysql.connector

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server (update credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Dohardthings1.1"  # Leave empty if no password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
