import os
import pandas as pd
import json

def merge_csv():
    filenames = []
    for i in os.listdir():
        if "customers-" in i:
            filenames += [i]
    dfs = [pd.read_csv(filename) for filename in filenames]
    res_df = pd.concat(dfs)
    res_df.to_csv("merged_dataframe.csv")
    # os.system('rm customers-*.csv')

def merge_customer2transaction():
    filenames = []
    for i in os.listdir():
        if "customer2transaction-" in i:
            filenames += [i]
    res = {}
    jsons = [json.load(open(filename)) for filename in filenames]
    result = []
    for d in jsons:
        result += d
    # os.system('rm customer2transaction-*.json')
    open('customer2transaction.json','w').write(json.dumps(result))

def merge_company2transaction():
    filenames = []
    for i in os.listdir():
        if "company2transaction-" in i:
            filenames += [i]
    res = {}
    jsons = [json.load(open(filename)) for filename in filenames]
    for d in jsons:
        for company in d:
            try: res[company] += d[company]
            except: res[company] = d[company]
    # os.system('rm company2transaction-*.json')
    open('company2transaction.json','w').write(json.dumps(res))

if __name__ == '__main__':
    merge_csv()
    merge_customer2transaction()
    merge_company2transaction()
