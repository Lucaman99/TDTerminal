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

pd.options.display.float_format = '{:.2f}'.format

# Reads filters that have been inputted

def inputs(age, occupation, income, education, relationship, balances):

    return {"age":age, "occupation":occupation, "income":income, "education":education, "relationship":relationship, "balances":balances}

# Reads a transaction history for each individual (set selection amount and timeframe (different timeframes can be plotted against each other)),
# and puts it into a table, with each row corresponding to a transaction with place, amount, time, and category

def selection_data(select_num, timeframe):

    filter_vars = inputs(age="", occupation="", income=[18566.75, 28742.0], education="", relationship="", balances="")
    data_store = []
    id_list = []
    filtering_val = {}
    for x, y in filter_vars.items():
        if (y != ""):
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

    print(data_store)

selection_data(0, 0)
