import numpy as np 
import pandas as pd 
import json
import random
import pdb
import os
import codecs 
import multiprocessing

def print_all_lengths(data):
    for key, value in data.items():
        print(f'{key}: {len(value)}')

job_classes = ["management", "business", "natural", "health", "education, law, society and government",
               "art, culture and sport", "sales and services", "trades, transport and equipment operators",
               "natural resourcs, agriculture", "manufacturing"]
skill_classes = ["A", "A", "B", "B", "C", "C", "D", "D"]

def get_job_and_skill(occupation_string):
    skill_class = "N/A"
    #print(occupation_string)
    if occupation_string[0] == "N" or occupation_string == "Retired":
        return ("N/A", "N/A")
    first_letter = occupation_string[0]
    if int(first_letter) in list(range(0,9)):
        job_class = job_classes[int(first_letter)]
        #skill_class = skill_classes[int(first_letter)]
    
        return (job_class, skill_class)
    return ("N/A", "N/A")
        
    

def bank_data_to_df(filename, idx):
    dic = json.load(codecs.open(filename, 'r', 'utf-8-sig'))
    dic = clean_dictionary(dic)
    #pdb.set_trace()
    
    surname = []
    givenname = []
    longitude = []
    latitude = []
    province = []
    age = []
    occupation = []
    relationship = []
    accounttype = []
    income = []
    ids = []
    types = []
    is_citizen = []
    credit_acc_id = []
    deposit_acc_id = []
    credit_acc_balance = []
    deposid_acc_balance = []
    jobs = []
    skills = []

    for cos in dic["customers"]:
        
        try:
            cit = clean_dictionary(cos["citizen"])
            per = clean_dictionary(cit["person"])
            adr = clean_dictionary(cit["addresses"])
            
            ids.append(cos["id"])
            surname.append(per["surname"])
            givenname.append(per["givenname"])
            longitude.append(adr["principalresidence"]["longitude"])
            latitude.append(adr["principalresidence"]["latitude"])
            province.append(adr["principalresidence"]["province"])
            age.append(per["age"])
            
            try:
                occupation = per["primaryoccupation"]
            except:
                occupation = "N/A"

            job, skill = get_job_and_skill(occupation)
            jobs.append(job)
            skills.append(skill)
            try:
                relationship.append(per["relationshipstatus"])
            except:
                relationship.append('None')    
            #pdb.set_trace()
            try:
                income.append(cit["totalincome"])
            except:
                income.append(0)
        except Exception as e:
            #print(per.keys())
            raise e
            continue
    
    cleaned_data = { "id": ids,
                    "surname":surname,
                    "givenname": givenname,
                    "longitude": longitude,
                    "latitude": latitude,
                    "province": province,
                    "age":age,
                    "relationship":relationship,
                    "jobs": jobs,
                    "skills":skills,
                    "income": income
                    }
    # pdb.set_trace()
    df = pd.DataFrame.from_dict(cleaned_data)
    df.to_csv(f"customers-{idx}.csv")

def transactions_to_json(filename, idx):
    transactions = json.load(codecs.open(filename, 'r', 'utf-8-sig'))
    transactions = list(map(clean_dictionary, transactions))

    customer2transactions = {}
    for account in transactions:
        #pdb.set_trace()
        try:
            customer_id = account["relatedcustomers"]["individual"][0]["customerid"]
        except:
            try:
                customer_id = account["relatedcustomers"]["authorized"][0]["customerid"]
            except:
                continue
        
        for transaction in account["transactions"]:
            #pdb.set_trace()
            try:
                merchant_category = transaction["merchantcategorycode"]
            except:
                continue
            try:
                new_transaction = {"city": transaction["locationcity"],
                                "region": transaction["locationregion"],
                                "latitude": transaction["locationlatitude"],
                                "longitude": transaction["locationlongitude"],
                                "amount" : transaction["currencyamount"],
                                "merchantName": transaction["merchantname"],
                                "merchantCategoryCode": int(merchant_category)
                                }
                #pdb.set_trace()
                customer2transactions[customer_id] = new_transaction

            except:
                continue
            

    with open( f"customer2transaction-{idx}.json", "w") as file:
        json.dump(customer2transactions, file)
    with open(f"company2transaction-{idx}.json", "w") as file:
        json.dump(company_to_transactions(customer2transactions), file)

def company_to_transactions(customer_to_transactions):
    company2transactions = {}
    for i, (idd, transaction) in enumerate(customer_to_transactions.items()):
        #pdb.set_trace()
        try:
            company = transaction["merchantName"]
        except:
            continue
        new_transaction = transaction
        new_transaction["id"] = idd
        try:
            company2transactions[company].append(new_transaction)
        except:
            company2transactions[company] = [new_transaction]

    return company2transactions

def clean_dictionary(dic):
    for key, value in dic.items():
        new_key = key.lower()
        del dic[key]
        if isinstance(value, dict):
            value = clean_dictionary(value)
        if isinstance(value, list):
            if len(value) > 0 and isinstance(value[0], dict):
                value = list(map(clean_dictionary, value))
        dic[new_key] = value
    
    return dic


if __name__ == "__main__":
    threads = []
    for i in os.listdir("data"):
        if "TD-World-Bank-v2.0" in i:
            print(i)
            idx = i.split(".")[-2].split("-")[-1].replace("_results","")
            t = multiprocessing.Process(target=bank_data_to_df,args=("data/TD-World-Bank-v2.0-%s_results.json" % idx, idx,))
            t2 = multiprocessing.Process(target=transactions_to_json, args=("data/TD-World-BankTransactions-v2.0-%s.json" % idx, idx,))
            t.start()
            t2.start()
            threads += [t,t2]

            if len(threads) == 8:
                for i in threads:
                    i.join()
                threads = []
