import json, re


def get_co(var, company, data_rng=10, r=json.load(open('../../company2transaction.json')), ci=json.load(open('../../calderdata/customerIndex.json'))):

	rng = {}
	blah = {}

	prefix = ""

	if var == "age":
		for trans in r[company]:
			cont = trans["amount"]
			_id = trans["id"]
			user = ci[_id]
			age = (user["citizen"]["person"]["age"] // data_rng) * data_rng
			if age not in rng:
				rng[age] = {
					"revenue" : 0,
					"quantity" : 0
				}
			rng[age]["revenue"] += cont
			rng[age]["quantity"] += 1
	elif var == "salary":
		prefix = "$"
		data_rng = 10000
		for trans in r[company]:
			cont = trans["amount"]
			_id = trans["id"]
			user = ci[_id]
			if "totalIncome" not in user["citizen"]:
				user["citizen"]["totalIncome"] = 0
			income = (user["citizen"]["totalIncome"] // data_rng) * data_rng
			if income not in rng:
				rng[income] = {
					"revenue" : 0,
					"quantity" : 0
				}
			rng[income]["revenue"] += cont
			rng[income]["quantity"] += 1
	elif var == "occupation":
		for trans in r[company]:
			cont = trans["amount"]
			_id = trans["id"]
			user = ci[_id]
			if "primaryOccupation" not in user["citizen"]["person"]:
				continue
			sp = user["citizen"]["person"]["primaryOccupation"].split(" ")
			occup = sp[0]
			name = " ".join(sp[1:])
			blah[occup] = name

			if occup not in rng:
				rng[occup] = {
					"revenue" : 0,
					"quantity" : 0
				}
			rng[occup]["revenue"] += cont
			rng[occup]["quantity"] += 1
	l = []
	if var == "occupation":
		for i in rng:
			rng[i]["value"] = blah[i]
			rng[i]["range"] = "N/A"
			l.append(rng[i])
	else:
		for i in rng:
			rng[i]["value"] = prefix + str(int(i)) + ' - ' +  prefix + str(int(i+data_rng))
			rng[i]["range"] = data_rng
			l.append(rng[i])

	l.sort(key=lambda key:key["revenue"], reverse=True)
	for i in range(len(l)):
		l[i]["rank"] = i + 1
		l[i]["revenue"] = "{:,}".format(int(l[i]["revenue"]))
		l[i]["quantity"] = "{:,}".format(int(l[i]["quantity"]))

	return l


if __name__ == '__main__':
	d = get_co("occupation","Tim Hortons")

	for i in d:
		print(i)