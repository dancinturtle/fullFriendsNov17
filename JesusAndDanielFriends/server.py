from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def home():
    query = "SELECT name, age, concat_ws(' ', MONTHNAME(date_of_friendship), DAY(date_of_friendship)) as dateOf, YEAR(date_of_friendship) as yearOf FROM friends"
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends)
@app.route('/add_friend', methods=['POST'])
def add_friend():
    query = "INSERT INTO friends (name, age, date_of_friendship) VALUES (:name, :age, NOW())"
    data = {
            'name': request.form['fullName'],
            'age':  request.form['friendAge'],

            }


    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)