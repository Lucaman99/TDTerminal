from flask import Flask
from flask import jsonify
from flask import request
from flask import send_from_directory

import cw_process
import json
app = Flask(__name__, static_url_path="", static_folder="../web/public")

r = json.load(open('../../company2transaction.json'))
ci = json.load(open('../../calderdata/customerIndex.json'))
@app.route("/getMarkets")
def getMarketsHandler():
	company = request.args.get("company")
	var = request.args.get("var")
	"""
	d = [
		{
			"rank" : i + 1,
			"gender" : random.choice(["Male", "Female", "Other"]),
			"age" : random.randint(10,80),
			"work" : random.choice(["Full Time", "Part Time", "Self Employed"]),
			"income" : random.randint(10,200) * 1000,
			"school" : random.choice([True,False]),
			"arrangement" : random.choice(["Married", "Single", "Divorced"]),
			"balance" : random.randint(0,20000)
		}
		for i in range(10)
	]
	"""
	d = cw_process.get_co(var, company, r=r, ci=ci)

	return jsonify(d)

@app.route('/')
def index():
    return app.send_static_file('index.html')

app.run(host='localhost', port=8080)