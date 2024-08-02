from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def form():
    return open('index.html').read()

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    
    # Connect to SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Insert form data into the database
    cursor.execute("INSERT INTO user (name, email, subject, message) VALUES (?, ?, ?, ?)", 
                   (name, email, subject, message))
    
    conn.commit()
    conn.close()
    
    return 'New record created successfully'

if __name__ == '__main__':
    app.run(debug=True)
