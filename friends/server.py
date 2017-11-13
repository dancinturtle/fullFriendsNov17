from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'myfriend')
@app.route('/')
def index():
    query = "SELECT * FROM myfriends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    
    query = "INSERT INTO myfriends (first_name, last_name, age, friend_since) VALUES (:first_name, :last_name, :age, NOW())"
    
    
    data = {
        
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'age': request.form['age'],
            }
    # add a friend to the database!
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)

# updating records
# @app.route('/update_friend/<friend_id>', methods=['POST'])
# def update(friend_id):
#     query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
#     data = {
#              'first_name': request.form['first_name'],
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation'],
#              'id': friend_id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')

# Deleting records

# @app.route('/remove_friend/<friend_id>', methods=['POST'])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': friend_id}
#     mysql.query_db(query, data)
#     return redirect('/')