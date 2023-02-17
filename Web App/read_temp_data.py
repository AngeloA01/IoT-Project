# import requests
# db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"


# def get_temperature():
#         response = requests.get(db+"/Temperature.json")
#         temperature = response.json()
#         temp_list = list(temperature.values())
#         k=0
#         sum=0
#         while (k<len(temp_list)):
#             p = temp_list[k]
#             p1 = p["Temperature"]
#             sum = sum + p1
#             k+=1
#         avg = sum/k
#         return round(avg, 1)
# print(get_temperature())


from firebase_admin import credentials, db
import time


def get_Temperature():
    ref = db.reference('/Temperature')
    Temperature_list = []
    while True:
        Temperature_snapshots = ref.order_by_key().limit_to_last(5).get()
        Temperature_list = [snapshot['Temperature'] for key, snapshot in Temperature_snapshots.items() if 'Temperature' in snapshot]
        if len(Temperature_list) == 5:
            break
        time.sleep(1) # wait for database to have 5 values
    
    avg = sum(Temperature_list) / len(Temperature_list)
    return round(avg, 1)

    # print(get_Temperature())