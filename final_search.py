from __future__ import print_function

import math

from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# from sklearn import metrics
# import tensorflow as tf
# from tensorflow.python.data import Dataset

pd.options.display.float_format = '{:.0f}'.format

company = "Starbucks"

# Reads filters that have been inputted

def inputs(a1, a2, i1, i2, education, relationship, b1, b2):

    # b1 and b2 (balance range) is deprecated

    return {"age":range(a1, a2), "income":range(i1, i2), "education":education, "relationship":relationship}

# Reads a transaction history for each individual (set selection amount and timeframe (different timeframes can be plotted against each other)),
# and puts it into a table, with each row corresponding to a transaction with place, amount, time, and category

def selection_data():

    filter_vars = inputs(a1=20, a2=40, i1=10000, i2=20000, education="", relationship="", b1=5000, b2=9000)
    data_store = []
    id_list = []
    filtering_val = {}
    for x, y in filter_vars.items():
        if (y != ""):
            filtering_val[x] = y


    get_data_users = pd.read_csv("merged_dataframe.csv", sep=",")


    for u in range (0, len(get_data_users)):
        indicator = False
        for x, y in filtering_val.items():
            # This assumes that the object labels are the same between the csv file and this program
            if (get_data_users.iloc[u][x] in y):
                indicator = True
            else:
                indicator = False
        if (indicator == True):
            id_list.append(get_data_users.iloc[u]["id"])




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

    # This isn't statistically sound but whatever
    average_amount_spent = 0
    
    for a in data_store:
        if (a['merchantName'] == company):
            average_amount_spent = average_amount_spent + int(a['currencyAmount'])
            counter = counter + 1
    average_amount_spent = average_amount_spent_total / counter

    for b in data_store:
        print(b['merchantName'])
        if (b['merchantName'] == company):
            median.append(int(a['currencyAmount']))
    median.sort()
    if (len(median)%2 == 0):
        print(median)
        wan = median[int(len(median)//2) - 1]
        true_median = (wan + median[int(len(median)//2)])//2
    else:
        true_median = median[int((len(median)-1)//2)]

    for a in range(0, len(get_data_transaction)):
        if (get_data_transaction.iloc[a]['merchantName'] == company):
            all_total = all_total + int(get_data_transaction.iloc[a]['currencyAmount'])
            counter2 = counter2 + 1
    average_overall = all_total / counter2

    final_thing_percent_money =  average_amount_spent_total / all_total
    final_thing_percent_people = (counter - 1) / (counter2 - 1)

    # Ranks locations, in terms of transaction amount, and number of transactions

    '''

    places = []
    for a in data_store:
        if (a['merchantName'] == company):
            places.append([a['longitude'], a['latitude']])

    location_data_coordinates = []
    location_data_numbers = []
    while (len(places) > 0):

        selector = places[0]
        location_data_coordinates.append(selector)
        del places[0]
        count_it_up = 0
        if (len(places) > 0):
            for j in range (0, len(places)):
                if (selector == places[j]):
                    count_it_up = count_it_up + 1

        location_data_numbers.append(count_it_up)


    '''

selection_data()


    # Creates a chart showing which categories the most money, the most transactions, and the greatest percentage of total transactions (amount of money and number of transactions)
    # (all in fixed amount of time)

    # Makes some suggestions to the company


#age, income, education, relationship, balances
