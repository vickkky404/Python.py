# PROJECT: To-Do List in Python
"""Features: 
1. Add Task
2. View all Tasks
3. Mark as Completed
4. Remind for the Task
5. Delete Task
"""

import time
from datetime import datetime

tasks = []  # List to store tasks

# Function to add a new task with a reminder
def add_task():
    task_name = input("Enter Task: ")
    reminder_time = input("Enter Reminder Time (HH:MM 24-hour format): ")

    try:
        reminder_datetime = datetime.strptime(reminder_time, "%H:%M").time()
        tasks.append({"task": task_name, "reminder": reminder_datetime})
        print("✅ Task Added Successfully!")
    except ValueError:
        print("❌ Invalid time format! Please enter time in HH:MM format.")

# Function to view all tasks in the list
def view_tasks():
    if not tasks:
        print("📌 No tasks found!")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['task']} - Reminder at {task['reminder']}")

# Function to check for due tasks in the list
def check_reminders():
    while True:
        now = datetime.now().time()  # Get current time
        for task in tasks[:]:  # Iterate over a copy of the list to allow removal
            if task["reminder"].hour == now.hour and task["reminder"].minute == now.minute:
                print(f"\n🔔 Reminder: {task['task']} is due now!")
                tasks.remove(task)  # Remove task after reminder
        
        time.sleep(30)  # Check every 30 seconds

# Main loop of the program
while True:
    print("\n--- 📝 To-Do List Manager ---")
    print("1. Add Task with Reminder")
    print("2. View Tasks")
    print("3. Start Reminder Service")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("⏳ Reminder service started. Keep this window open.")
        check_reminders()
    elif choice == "4":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please try again.")
