from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import datetime

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html', all_friends=friends)

@app.route('/add', methods=['POST'])
def add_new():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    age = request.form['age']
    date_since = request.form['since']
    query = "INSERT INTO friends(first_name, last_name, age, friend_since) VALUES(:first_name, :last_name, :age, :friend_since)"
    data = {
        "first_name": firstname,
        "last_name": lastname,
        "age": age,
        "friend_since": date_since
    }

    mysql.query_db(query, data)
    return redirect('/')

    
app.run(debug=True)