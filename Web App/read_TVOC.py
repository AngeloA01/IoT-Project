# import requests
# db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"


# def get_TVOC():
#         response = requests.get(db+"/TVOC.json")
#         TVOC = response.json()
#         TVOC_list = list(TVOC.values())
#         k=0
#         sum=0
#         while (k<len(TVOC_list)):
#             p = TVOC_list[k]
#             p1 = p["TVOC"]
#             sum = sum + p1
#             k+=1
#         avg = sum/k
#         return round(avg, 1)
# print(get_TVOC())

import firebase_admin
from firebase_admin import credentials, db
import time


def get_TVOC():
    ref = db.reference('/TVOC')
    TVOC_list = []
    while True:
        TVOC_snapshots = ref.order_by_key().limit_to_last(5).get()
        TVOC_list = [snapshot['TVOC'] for key, snapshot in TVOC_snapshots.items() if 'TVOC' in snapshot]
        if len(TVOC_list) == 5:
            break
        time.sleep(1) # wait for database to have 5 values
    
    avg = sum(TVOC_list) / len(TVOC_list)
    return round(avg, 1)

# print(get_TVOC())