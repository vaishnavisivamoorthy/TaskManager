# db.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # use your MySQL username
        password="root",  # replace with your MySQL password
        database="task_manager"
    )
