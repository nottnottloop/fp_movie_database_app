import requests
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template

server = Flask(__name__)

@server.route('/') 
@server.route('/index') 
def home(): 
	movies = []
	ids = ['tt3896198', 'tt0111161', 'tt0499549', 'tt0082971', 'tt0325980', 'tt0295297']
	for id in ids: 
		r = requests.get(f"http://www.omdbapi.com/?i={id}&apikey=d9ba51a5")
		data = r.json()
		movies.append(data)
	return render_template('index.html', movies=movies)

server.run(debug=True)