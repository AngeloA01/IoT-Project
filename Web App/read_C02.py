# import requests
# db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"


# def get_C02():
    
#         response = requests.get(db+"/C02.json")
#         C02 = response.json()
#         C02_list = list(C02.values())
#         k=0
#         sum=0
#         while (k<len(C02_list)):
#             p = C02_list[k]
#             p1 = p["C02"]
#             sum = sum + p1
#             k+=1
#         avg = sum/k
#         return round(avg, 1)
# print(get_C02())

import firebase_admin
from firebase_admin import credentials, db
import time


def get_C02():
    ref = db.reference('/C02')
    c02_list = []
    while True:
        c02_snapshots = ref.order_by_key().limit_to_last(5).get()
        c02_list = [snapshot['C02'] for key, snapshot in c02_snapshots.items() if 'C02' in snapshot]
        if len(c02_list) == 5:
            break
        time.sleep(1) # wait for database to have 5 values
    
    avg = sum(c02_list) / len(c02_list)
    return round(avg, 1)

# print(get_C02())