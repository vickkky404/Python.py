from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Function to connect to database
def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        task = request.form["task"]
        reminder = request.form["reminder"]
        cursor.execute("INSERT INTO tasks (task, reminder) VALUES (?, ?)", (task, reminder))
        conn.commit()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    # ✅ Make sure Flask loads the correct HTML template
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>", methods=["POST"])
def delete_task(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
