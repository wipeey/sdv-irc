import bcrypt
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('db/database.db')

@app.route('/register', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Connect to the database and insert the data
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

    return redirect(url_for('success'))

@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']

    # Check if the user exists and compare hashed password
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    stored_password = cursor.fetchone()

    if stored_password and bcrypt.checkpw(password.encode('utf-8'), stored_password[0]):
        # Password matches, proceed with login
        return redirect(url_for('success'))
    else:
        # Incorrect username or password
        return "Login failed! Invalid credentials."

@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
