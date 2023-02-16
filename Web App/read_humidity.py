import requests

db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"
def get_humidity():
        
        response = requests.get(db+"/Humidity.json")
        Humidity = response.json()
        hum_list = list(Humidity.values())
        k=0
        sum=0
        while (k<len(hum_list)):
            p = hum_list[k]
            p1 = p["Humidity"]
            sum = sum + p1
            k+=1
        avg = sum/k
        return round(avg, 1)
print(get_humidity())