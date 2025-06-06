# task_agent.py
from db import get_connection
from parser_task import parse_task

def add_task(text):
    title, due_date, priority = parse_task(text)
    status = "pending"

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, due_date, priority, status) VALUES (%s, %s, %s, %s)",
        (title, due_date, priority, status)
    )
    conn.commit()
    conn.close()
    print(f"✅ Task added: {title} | Due: {due_date} | Priority: {priority}")

def list_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, due_date, priority, status FROM tasks")
    for (id, title, due_date, priority, status) in cursor.fetchall():
        print(f"{id}. [{priority}] {title} | Due: {due_date} | Status: {status}")
    conn.close()
