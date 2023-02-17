# import requests
# db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"
# def get_humidity():
#         response = requests.get(db+"/Humidity.json")
#         Humidity = response.json()
#         hum_list = list(Humidity.values())
#         k=0
#         sum=0
#         while (k<len(hum_list)):
#             p = hum_list[k]
#             p1 = p["Humidity"]
#             sum = sum + p1
#             k+=1
#         avg = sum/k
#         return round(avg, 1)
# print(get_humidity())

import firebase_admin
from firebase_admin import credentials, db
import time


def get_Humidity():
    ref = db.reference('/Humidity')
    Humidity_list = []
    while True:
        Humidity_snapshots = ref.order_by_key().limit_to_last(5).get()
        Humidity_list = [snapshot['Humidity'] for key, snapshot in Humidity_snapshots.items() if 'Humidity' in snapshot]
        if len(Humidity_list) == 5:
            break
        time.sleep(1) # wait for database to have 5 values
    
    avg = sum(Humidity_list) / len(Humidity_list)
    return round(avg, 1)
