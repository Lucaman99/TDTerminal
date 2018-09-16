from __future__ import print_function

import math

from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

pd.options.display.float_format = '{:.1f}'.format

# Reads filters that have been inputted

def inputs(gender, age, work, income, school, arrangement, balance):

    return {"gender":gender, "age":age, "work":work, "income":income, "school":school, "arrangement":arrangement, "balance":balance}

# Reads a transaction history for each individual (set selection amount and timeframe (different timeframes can be plotted against each other)),
# and puts it into a table, with each row corresponding to a transaction with place, amount, time, and category

def selection_data(select_num, timeframe):

    filter_vars = inputs(gender="", age="", work="test", income="test", school="test", arrangement="test", balance="")
    data_store = []
    id_list = []
    filtering_val = {}
    for x, y in filter_vars.items():
        if (len(y) > 0):
            filtering_val[x] = y

    print(filtering_val)

    get_data_users = pd.read_csv("placeholder2.csv", sep=",")

    for u in range (0, len(get_data_users)):
        indicator = False
        for x, y in filtering_val.items():
            # This assumes that the object labels are the same between the csv file and this program
            if (get_data_users[u][x] == y):
                indicator = True
            else:
                indicator = False
        if (indicator == True):
            id_list.append(get_data_users[u]["id_placeholder"])


    get_data_transaction = pd.read_csv("placeholder.csv", sep=",")

    for i in range (0, len(get_data_transaction)):
        if (get_data_transaction["id_placeholder"] in id_list):
            data_store.append(get_data_transaction[i])

selection_data(0, 0)


# Finds the average and median for transaction amount, percentage of total transactions (amount of money and number of transactions), and number of transactions
#(all in a set timeframe) for the company and show them

# Creates a graph for top 10 locations, in terms of transaction amount, and number of transactions

# Creates a chart showing which categories the most money, the most transactions, and the greatest percentage of total transactions (amount of money and number of transactions)
# (all in fixed amount of time)

#Makes some suggestions to the company
