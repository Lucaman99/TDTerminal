import json
import os


def create_index(filename):
	d = json.load(open(filename))

	o = {}
	for i in d["customers"]:
		o[i["id"]] = i

	return o
def update_index(data, filename):
	d = json.load(open(filename))
	for i in data:
		d[i] = data[i]

	open(filename,'w').write(json.dumps(d, indent=4))


def destroy_index(filename):
	open(filename)



if __name__ == '__main__':
	for i in os.listdir("../data"):
		if "TD-World-Bank-v2.0" in i:
			print(i)
			update_index(
				create_index("../data/" + i),
				"customerIndex.json")
