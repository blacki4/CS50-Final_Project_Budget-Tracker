from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Secret key for managing user sessions

DB_PATH = "database.db"  # SQLite database file path


# -------------------------------
# Helper function to connect to DB
# -------------------------------
def get_db_connection():
    # Creates a new connection to the SQLite database
    # row_factory allows us to access rows as dictionaries (row["column"])
    conn = sqlite3.connect(DB_PATH, timeout=10)  # Added timeout for reliability
    conn.row_factory = sqlite3.Row
    return conn


# -------------------------------
# Home page (redirect if logged in)
# -------------------------------
@app.route("/")
def home():
    if 'user_id' in session:
        return redirect("/dashboard")
    return render_template("index.html")


# -------------------------------
# User registration
# -------------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]  # ⚠️ Plain text storage (not secure, just for learning!)
        try:
            with get_db_connection() as conn:
                conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
        except sqlite3.IntegrityError:
            # Handles case where username already exists
            return render_template("register.html", error="Username already exists")
        return redirect("/login")
    return render_template("register.html")


# -------------------------------
# User login
# -------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        with get_db_connection() as conn:
            user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)).fetchone()
        if user:
            # Save session data (user is logged in)
            session['user_id'] = user["id"]
            session['username'] = user["username"]
            return redirect("/dashboard")
        return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")


# -------------------------------
# Logout
# -------------------------------
@app.route("/logout")
def logout():
    session.clear()  # Clear session data
    return redirect("/")


# -------------------------------
# Dashboard page
# -------------------------------
@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect("/login")
    with get_db_connection() as conn:
        # Get all transactions for this user, newest first
        transactions = conn.execute(
            "SELECT * FROM transactions WHERE user_id=? ORDER BY date DESC",
            (session['user_id'],)
        ).fetchall()
    return render_template("dashboard.html", transactions=transactions)


# -------------------------------
# Add new transaction
# -------------------------------
@app.route("/add", methods=["POST"])
def add_transaction():
    if 'user_id' not in session:
        return redirect("/login")

    # Extract transaction data from form
    amount = float(request.form["amount"])
    category = request.form["category"]
    date = request.form["date"]
    t_type = request.form["type"]  # income or expense

    try:
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO transactions (user_id, amount, category, date, type) VALUES (?, ?, ?, ?, ?)",
                (session['user_id'], amount, category, date, t_type)
            )
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Database error:", e)

    return redirect("/dashboard")


# -------------------------------
# Delete transaction
# -------------------------------
@app.route("/delete/<int:id>")
def delete_transaction(id):
    if 'user_id' not in session:
        return redirect("/login")
    try:
        with get_db_connection() as conn:
            conn.execute("DELETE FROM transactions WHERE id=? AND user_id=?", (id, session['user_id']))
            conn.commit()
    except sqlite3.OperationalError as e:
        print("Database error:", e)
    return redirect("/dashboard")


# -------------------------------
# Expense summary (JSON for charts)
# -------------------------------
@app.route("/summary")
def summary():
    if 'user_id' not in session:
        return jsonify({})
    with get_db_connection() as conn:
        data = conn.execute(
            "SELECT category, SUM(amount) as total FROM transactions WHERE user_id=? AND type='expense' GROUP BY category",
            (session['user_id'],)
        ).fetchall()
    result = {row["category"]: row["total"] for row in data}
    return jsonify(result)


# -------------------------------
# Income summary (JSON for charts)
# -------------------------------
@app.route("/income_summary")
def income_summary():
    if 'user_id' not in session:
        return jsonify({})
    with get_db_connection() as conn:
        data = conn.execute(
            "SELECT category, SUM(amount) as total FROM transactions WHERE user_id=? AND type='income' GROUP BY category",
            (session['user_id'],)
        ).fetchall()
    result = {row["category"]: row["total"] for row in data}
    return jsonify(result)


# -------------------------------
# Main entry point
# -------------------------------
if __name__ == "__main__":
    # NOTE:
    # - This project was developed as part of CS50 final project.
    # - I wrote the main logic myself, but I used AI tools like ChatGPT and Claude
    #   as helpers for debugging, code suggestions, and improving readability.
    # - All design decisions and final implementation were done by me.
    app.run(debug=True)
