from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    query = "SELECT * FROM friends"                           
    friends = mysql.query_db(query)                          
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (name, age, friend_since) VALUES (:name, :age, :friend_since)"
    
    data = {
             'name': request.form['name'],
             'age':  request.form['age'],
             'friend_since': request.form['friend_since'],
           }
   
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)

