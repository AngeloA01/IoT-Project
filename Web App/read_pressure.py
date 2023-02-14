import requests
db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"
def get_pressure():
        response = requests.get(db+"/pressure/.json")
        pressure = response.json()
        pressure_list = list(pressure.values())
        k=0
        sum=0
        while (k<len(pressure_list)):
            p = pressure_list[k]
            p1 = p["pressure: "]
            sum = sum + p1
            k+=1
        avg = sum/k
        return round(avg, 1)
print(get_pressure())