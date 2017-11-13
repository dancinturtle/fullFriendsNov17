from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')


@app.route('/')
def index():
    query = "SELECT full_name, age, year, concat_ws(' ', monthname(friends_since), day(friends_since)) as dateOf FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (full_name, age, year, friends_since) VALUES (:full_name, :age, year(NOW()), NOW())"
    data = {
             'full_name': request.form['full_name'],
             'age':  request.form['age'],
            #  'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>')
def show(friend_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_friend=friends[0])
app.run(debug=True)

@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET fUll_name = :full_name, age = :age WHERE id = :id"
    data = {
             'full_name': request.form['full_name'],
             'age':  request.form['age'],
            #  'occupation': request.form['occupation'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')

