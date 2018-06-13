import json

from flask import Flask, render_template
import pandas as pd
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.agile


app = Flask(__name__)

@app.route("/")
def index():
	df = pd.read_csv('data.csv').drop('Open', axis=1)
	chart_data = df.to_dict(orient='records')
	chart_data = json.dumps(chart_data, indent=2)
	data = {'chart_data': chart_data}

	print data
	return render_template("index.html", data=data)

@app.route("/login")
def login():
	df = pd.read_csv('data.csv').drop('Open', axis=1)
	chart_data = df.to_dict(orient='records')
	chart_data = json.dumps(chart_data, indent=2)
	data = {'chart_data': chart_data}
	return render_template("login.html", data=data)

@app.route("/d3plot")
def d3plot():

	collection = db['d3example']
	cursor = collection.find({})
	chart_data = []
	for document in cursor:
		# document.pop['_id']
		document = {'Date':document['Date'],'High':float(document['High']), 'Low':float(document['Low']),'Close':float(document['Close']) }
		chart_data.append(document)

	chart_data = json.dumps(chart_data, indent=2)
	data = {'chart_data': chart_data}

	print data

	# df = pd.read_csv('data.csv').drop('Open', axis=1)
	# chart_data = df.to_dict(orient='records')
	# chart_data = json.dumps(chart_data, indent=2)
	# data = {'chart_data': chart_data}
	return render_template("d3plotExample.html", data=data)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

# mongoimport -d agile -c d3example --type csv --file data.csv --headerline