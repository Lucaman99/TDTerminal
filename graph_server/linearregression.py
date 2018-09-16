# add conclusion statement 
# add different features for comparisions
# possible features: (num for trend) age, income, account balance, spending (income - balance) || (classify)noc, province, relationship

#importing stuff
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import csv
import pandas as pd
import scipy
from sklearn.linear_model import LinearRegression
from IPython import embed
from scipy.interpolate import *

#data extraction from csv file + dimension reduction + convert to panda dataframe
##the input1 could be age, income, or account balance
##the input2 could be age, income, account balance, province, NOC, relationship
def generatePlot(input1, input2):
	input1 = "age" #dependent variable, x axis
	input2 = "balances" #independent variable, y axis
	csv = "cleaned_data.csv" 
	df = pd.read_csv(csv)

	#data extraction from df + dimension reduction + convert to nparray from panda dataframe
	x = pd.DataFrame(df, columns = [input1]).as_matrix()[:,0]
	y = pd.DataFrame(df, columns = [input2]).as_matrix()[:,0]

	##Create simple linear model
	# model = LinearRegression(fit_intercept=True)
	# model.fit(x[:, np.newaxis], y)

	# xfit = np.linspace(0, 5, 50)
	# yfit = model.predict(xfit[:, np.newaxis])

	# embed()

	# A more usable linear model 
	p= np.polyfit (x,y,1) ##polyfit 1 deg

	#plotting
	plt.plot(x, np.polyval(p,x),'-r')
	plt.scatter(x, y)
	plt.xlabel(input1)
	plt.ylabel(input2)
	plt.title(input2+" vs "+input1)
	plt.savefig("static/"+input2+"_vs_"+input1+'.jpg')
	plt.show()



