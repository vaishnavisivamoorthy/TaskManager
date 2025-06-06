# TaskManager

# 🧠 AI-Based Task Manager Agent

This project is an **AI-powered Task Manager Agent** that accepts natural language task descriptions, extracts structured task data (like title, priority, and due date), and stores them in a MySQL database. It also reminds you about tasks at the right time through in-browser notifications.

---

## 🚀 Features

- ✍️ **Natural Language Input** – Add tasks like:  
  `"Remind me to submit the report next Friday at 10 AM. High priority."`
- 🧠 **AI Task Parser** – Extracts title, due date, and priority using NLP.
- 🗂️ **Task Viewer** – View all pending tasks.
- 🔔 **Smart Reminders** – Notifications popup exactly when a task is due.
- 🧱 **MySQL Integration** – All tasks are stored in a structured database.
- 🌐 **Flask Backend + JavaScript Frontend** – Lightweight and fast.

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, JavaScript (with SweetAlert & Notifications API)
- **Backend**: Python (Flask)
- **Database**: MySQL
- **NLP Engine**: spaCy + Dateparser

---

## 🗂️ Project Structure
task-manager-agent/
├── app.py # Flask server
├── parser_task.py # NLP task parser
├──main.py
├──db.py
├──task_agent.py
├── templates/
│ └── index.html # Main UI
├── requirements.txt
└── README.md

Install all the depedencies and setup MYSQL to create database and table. Update the mysql in app.py. Run the code, a localhost link will appear click the link and view output in browser.

Notes:

⏰ Reminder Notifications
**The browser checks for tasks every 60 seconds.
**Notifications appear when the current time matches the due_date.
**Uses JavaScript Notifications API and SweetAlert popups.
**Make sure to allow notifications in your browser when prompted!

🧠 How NLP Parsing Works
**We use spaCy and dateparser to extract:
**Title – The main task description
**Date/Time – Using natural language like "tomorrow at 5 PM"
**Priority – Keywords like "high", "urgent", etc.

💡 Future Improvements
✅ Edit / delete tasks
📧 Email/SMS reminders
