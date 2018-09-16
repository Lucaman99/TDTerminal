from __future__ import print_function
from flask import Flask, render_template, request
import json
import math

from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("frontend.html")

@app.route("/results")

def redirect():


     company = request.args["company"]

     # Reads filters that have been inputted

     def inputs(a1, a2, i1, i2, relationship, b1, b2):

         return {"age":range(a1, a2), "income":range(i1, i2), "relationship":[relationship], "balances":range(b1, b2)}

     # Reads a transaction history for each individual (set selection amount and timeframe (different timeframes can be plotted against each other)),
     # and puts it into a table, with each row corresponding to a transaction with place, amount, time, and category


     filter_vars = inputs(a1=int(request.args['a1']), a2=int(request.args['a2']), i1=int(request.args['i1']), i2=int(request.args['i2']), relationship=request.args['relationship'], b1=int(request.args['b1']), b2=int(request.args['b2']))
     print("This: "+str(filter_vars["age"]))
     data_store = []
     id_list = []
     filtering_val = {}
     for x, y in filter_vars.items():
         if (y != [""]):
             filtering_val[x] = y


     get_data_users = pd.read_csv("cleaned_data.csv", sep=",")


     for u in range (0, len(get_data_users)):
         indicator = False
         for x, y in filtering_val.items():
             # This assumes that the object labels are the same between the csv file and this program
             if (get_data_users.iloc[u][x] in y):
                 indicator = True
             else:
                 indicator = False
                 break
         if (indicator == True):
             id_list.append(get_data_users.iloc[u]["id"])

     print(len(id_list))


     get_data_transaction = pd.read_csv("out.csv", sep=",")

     for i in range (0, len(get_data_transaction)):
         if (get_data_transaction.iloc[i]["id"] in id_list):
             place = {}
             place['id'] = get_data_transaction.iloc[i]['id']
             place['city'] = get_data_transaction.iloc[i]['city']
             place['merchantCategoryCode'] = get_data_transaction.iloc[i]['merchantCategoryCode']
             place['merchantName'] = get_data_transaction.iloc[i]['merchantName']
             place['longitude'] = get_data_transaction.iloc[i]['longitude']
             place['latitude'] = get_data_transaction.iloc[i]['latitude']
             place['currencyAmount'] = get_data_transaction.iloc[i]['currencyAmount']
             data_store.append(place)

     # General search: Age percentages, average and mean income, education percentages, relationship percentages, average and mean balance


     # Finds the average and median for transaction amount, percentage of total transactions (amount of money and number of transactions), and number of transactions
     #(all in a set timeframe) for the company and show them

     average_amount_spent_total = 0
     counter = 1
     median = []
     true_median = 0
     all_total = 0

     average_transactions = 0
     counter2 = 1
     median2 = []
     true_median2 = []

     average_amount_spent = 0

     # This isn't statistically sound but whatever

     for a in data_store:
         if (a['merchantName'] == company):
             average_amount_spent_total = average_amount_spent_total + int(a['currencyAmount'])
             counter = counter + 1
     average_amount_spent = average_amount_spent_total / counter

     for b in data_store:
         if (b['merchantName'] == company):
             median.append(int(b['currencyAmount']))
     median.sort()
     if (len(median) > 0):
         if (len(median)%2 == 0):
             true_median = (median[int(len(median)/2) - 1] + median[int(len(median)/2)])/2
         else:
             true_median = median[int((len(median)-1)/2)]
     else:
         true_median = 0

     for c in range(0, len(get_data_transaction)):
         if (get_data_transaction.iloc[c]['merchantName'] == company):
             all_total = all_total + int(get_data_transaction.iloc[c]['currencyAmount'])
             counter2 = counter2 + 1
     average_overall = all_total / counter2

     for f in range(0, len(get_data_transaction)):
         if (get_data_transaction.iloc[f]['merchantName'] == company):
             median2.append(int(get_data_transaction.iloc[f]['currencyAmount']))
     median2.sort()
     if (len(median2)%2 == 0):
         true_median2 = (median2[int(len(median2)/2) - 1] + median2[int(len(median2)/2)])/2
     else:
         true_median2 = median2[int((len(median2)-1)/2)]

     print(average_amount_spent_total)
     print(all_total)

     final_thing_percent_money =  float(average_amount_spent_total) / all_total
     final_thing_percent_people = float(counter - 1) / (counter2 - 1)

     # Ranks locations, in terms of transaction amount, and number of transactions


     places = []
     for a in data_store:
         if (a['merchantName'] == company):
             places.append(a['city'])

     location_data_coordinates = []
     location_data_numbers = []

     for i in range (0, len(places)):
         if (places[i] not in location_data_coordinates):
             location_data_coordinates.append(places[i])
             summation = 0
             for j in range (0, len(places)):
                 if (places[i] == places[j]):
                     summation = summation + 1
             location_data_numbers.append(summation)


     one = "This demographic spends an average of: "+str(average_amount_spent)+" Dollars per visit to "+company
     two = "The median amount of money this demographic spends per visit to "+company+" is: "+str(true_median)+" Dollars"
     three = "Average amount of money that all demographics spend at "+company+": "+str(average_overall)+" Dollars"
     four = "Median amount of money that all demographics spend at "+company+": "+str(true_median2)+" Dollars"
     five = "Percentage of total income (from dataset) attributed to this demographic: "+str(100*final_thing_percent_money)+"%"
     six = "Percentage of total customers (from dataset) attributed to this demographic: "+str(100*final_thing_percent_people)+"%"
     seven = str([location_data_coordinates, location_data_numbers])



         # Creates a chart showing which categories the most money, the most transactions, and the greatest percentage of total transactions (amount of money and number of transactions)
         # (all in fixed amount of time)

         # Makes some suggestions to the company


     #age, income, education, relationship, balances

     form_dict = one+","+two+","+three+","+four+","+five+","+six+","+seven


     return render_template('result.html', result = form_dict)



if __name__ == "__main__":
    app.run(debug=True)
