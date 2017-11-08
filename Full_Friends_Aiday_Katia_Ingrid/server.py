from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friend')

@app.route('/')
def index():
    query = "SELECT * FROM friend"
    friend = mysql.query_db(query)
    return render_template('index.html', full_friend = friend)

@app.route('/process', methods=['POST'])
def add():
    print "Enter"
    query = "INSERT INTO friend (first_name, last_name, age, created_at) VALUES (:first_name, :last_name, :age, NOW())"
    print "Enter"
    data = {
        'first_name' : request.form['fname'],
        'last_name' : request.form['lname'],
        'age' : request.form['age']
    }
    print "Enter"
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)