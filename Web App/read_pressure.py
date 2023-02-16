# import requests
# db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"
# def get_pressure():
#         response = requests.get(db+"/Pressure.json")
#         pressure = response.json()
#         pressure_list = list(pressure.values())
#         k=0
#         sum=0
#         while (k<len(pressure_list)):
#             p = pressure_list[k]
#             p1 = p["Pressure"]
#             sum = sum + p1
#             k+=1
#         avg = sum/k
#         return round(avg, 1)
# print(get_pressure())

import firebase_admin
from firebase_admin import credentials, db
import time

def get_Pressure():
    ref = db.reference('/Pressure')
    Pressure_list = []
    while True:
        Pressure_snapshots = ref.order_by_key().limit_to_last(5).get()
        Pressure_list = [snapshot['Pressure'] for key, snapshot in Pressure_snapshots.items() if 'Pressure' in snapshot]
        if len(Pressure_list) == 5:
            break
        time.sleep(1) # wait for database to have 5 values
    
    avg = sum(Pressure_list) / len(Pressure_list)
    return round(avg, 1)

# print(get_Pressure())