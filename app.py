from flask import Flask, request, jsonify, render_template
from db import get_connection
from parser_task import parse_task
from datetime import datetime
import threading
import time
from plyer import notification  # For desktop notifications

app = Flask(__name__)

# Background reminder thread
def check_reminders():
    while True:
        try:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM tasks WHERE due_date <= %s AND status = 'pending'",
                (now,)
            )
            tasks = cursor.fetchall()
            for task in tasks:
                # Send desktop notification
                notification.notify(
                    title=f"Task Reminder: {task['title']}",
                    message=f"This task is due now!",
                    app_name="AI Task Manager",
                    timeout=10
                )
                # Mark as notified (optional)
                cursor.execute(
                    "UPDATE tasks SET status = 'notified' WHERE id = %s",
                    (task['id'],)
                )
                conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error in reminder thread: {e}")
        time.sleep(60)  # Check every minute

# Start reminder thread
reminder_thread = threading.Thread(target=check_reminders)
reminder_thread.daemon = True
reminder_thread.start()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_task():
    data = request.get_json()
    text = data.get("text")
    title, due_date, priority = parse_task(text)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, due_date, priority, status) VALUES (%s, %s, %s, %s)",
        (title, due_date, priority, "pending")
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "✅ Task added", "title": title})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    due_now = request.args.get('due_now')
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    if due_now:
        cursor.execute(
            "SELECT * FROM tasks WHERE due_date <= %s AND status = 'pending'",
            (due_now,)
        )
    else:
        cursor.execute("SELECT * FROM tasks ORDER BY due_date ASC")
        
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET status = 'completed' WHERE id = %s",
        (task_id,)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Task marked as completed"})

if __name__ == "__main__":
    app.run(debug=True)