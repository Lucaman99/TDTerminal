import json
import time
import glob
import os
<<<<<<< HEAD
=======
from linearregression import generatePlot
>>>>>>> 4884701cea72d955a6f8866d56c2d630253a2629
from shutil import copyfile
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from IPython import embed
<<<<<<< HEAD
from flask_thumbnails import Thumbnail


 
=======

>>>>>>> 4884701cea72d955a6f8866d56c2d630253a2629
app = Flask(__name__)

@app.route("/")
def main():
<<<<<<< HEAD
    return render_template('main.html')
=======
	return render_template('main.html')
>>>>>>> 4884701cea72d955a6f8866d56c2d630253a2629

@app.route("/graph", methods=['POST', 'GET'])
# input1 = request.args.get('input1')
def graph():
<<<<<<< HEAD
    return redirect('/?session=%s#try' % session_id)

if __name__ == "__main__":
    app.run(debug = True, port=3000)


=======
	input1 = request.args.get('input1')
	input2 = request.args.get('input2')
	generatePlot(input1, input2)
	print input1
	return render_template('main.html', input1=input1, input2=input2)

if __name__ == "__main__":
	app.run(debug = True, port=3000)
>>>>>>> 4884701cea72d955a6f8866d56c2d630253a2629
