from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import bleach

app = Flask(__name__)
app.secret_key = "thisisabigsecret"

mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    friends = mysql.query_db("select concat_ws(' ', first_name, last_name) as name, round(datediff(date(now()),dob)/365) as age, concat_ws(' ', monthname(friend_since), DATE_FORMAT(friend_since, '%D')) as friend_since, year(friend_since) as year from friends")
    print friends

    return render_template('index.html', all_friends=friends)


@app.route('/add_friend', methods=['POST'])
def add_friend():
    query = "insert into friends (first_name, last_name, dob, friend_since, created_at, updated_at) values (:first_name, :last_name, :dob, :friend_since, now(), now())"
    error = False

    if(len(bleach.clean(request.form['first_name'])) > 255):
        flash("First name cannot be longer than 255", "error")
        error = True
    if(len(bleach.clean(request.form['first_name'])) < 1):
        flash("First name cannot be empty", "error")
        error = True
    elif(len(bleach.clean(request.form['last_name'])) > 255):
        flash("Last name cannot be longer than 255", "error")
        error = True
    # elif(len(bleach.clean(request.form['last_name'])) < 1):
    #     flash("Last name cannot be longer than 255", "error")
    #     error = True

    print type(request.form['dob'])
   
    if not error:
        data = {
            'first_name' : bleach.clean(request.form['first_name']),
            'last_name' : bleach.clean(request.form['last_name']),
            'dob' : request.form['dob'],
            'friend_since' : request.form['friend_since']
        }
        friend_id = mysql.query_db(query, data)
    
    return redirect('/')

app.run(debug=True)
