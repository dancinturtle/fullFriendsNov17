from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import datetime

app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends')


@app.route('/')
def index():
    query = "SELECT name, age, DATE_FORMAT(created_at,'%M %D, %Y') AS since FROM friends" 
    friends = mysql.query_db(query)

    return render_template('friends.html', friend_list=friends)

@app.route('/process', methods=['POST'])
def add_friend():
    name = request.form['name']
    age = request.form['age']

    query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"

    data = {
        'name': request.form['name'],
        'age': request.form['age'],
        'created_at': datetime.datetime.now(),
        'updated_at': datetime.datetime.now()
    }
    mysql.query_db(query, data)

    return redirect('/')

app.run(debug=True)
