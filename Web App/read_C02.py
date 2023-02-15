import requests
db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"


def get_C02():
        response = requests.get(db+"/C02.json")
        C02 = response.json()
        C02_list = list(C02.values())
        k=0
        sum=0
        while (k<len(C02_list)):
            p = C02_list[k]
            p1 = p["C02"]
            sum = sum + p1
            k+=1
        avg = sum/k
        return round(avg, 1)
print(get_C02())