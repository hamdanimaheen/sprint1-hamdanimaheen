import flask
from flask import jsonify
from flask import request

from sql import create_connection
from sql import execute_read_query
from sql import execute_query

import creds

app = flask.Flask(__name__)
app.config["DEBUG"] = True


#-------------LOGIN API-------------#

#----------CRUD OPERATIONS----------#
#---------FLOOR TABLE CRUD----------#
#API 1.1 : GET
# the Endpoint is http://127.0.0.5:5002/floor/api/all
@app.route('/floor/api/all', methods=['GET'])
def floor_api_all():
#create connection
 myCreds = creds.Creds() # getting from creds.py file
 connection = create_connection(myCreds.connectionstring, myCreds.username, myCreds.password, myCreds.database)

 sql = "SELECT * FROM floor"
 floor = execute_read_query(connection, sql)
 return jsonify(floor)

#API 1.2 : POST
#API 1.3 : PUT
#API 1.4 : DELETE

#---------ROOM TABLE CRUD----------#
#API 2.1 : GET
# the Endpoint is http://127.0.0.5:5005/room/api/all
@app.route('/room/api/all', methods=['GET'])
def room_api_all():
#create connection
 myCreds = creds.Creds() # getting from creds.py file
 connection = create_connection(myCreds.connectionstring, myCreds.username, myCreds.password, myCreds.database)

 sql = "SELECT * FROM room"
 room = execute_read_query(connection, sql)
 return jsonify(room)

#API 2.2 : POST
#API 2.3 : PUT
#API 2.4 : DELETE

#---------RESIDENT TABLE CRUD----------#
#API 3.1 : GET
# the Endpoint is http://127.0.0.5:5005/resident/api/all
@app.route('/resident/api/all', methods=['GET'])
def resident_api_all():
#create connection
 myCreds = creds.Creds() # getting from creds.py file
 connection = create_connection(myCreds.connectionstring, myCreds.username, myCreds.password, myCreds.database)

 sql = "SELECT * FROM resident"
 room = execute_read_query(connection, sql)
 return jsonify(resident)

#API 3.2 : POST
#API 3.3 : PUT
#API 3.4 : DELETE


app.run(port=5005)
