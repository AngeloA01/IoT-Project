import requests
db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"


def get_temperature():
        response = requests.get(db+"/temperature/.json")
        temperature = response.json()
        temp_list = list(temperature.values())
        k=0
        sum=0
        while (k<len(temp_list)):
            p = temp_list[k]
            p1 = p["temperature: "]
            sum = sum + p1
            k+=1
        avg = sum/k
        return round(avg, 1)
print(get_temperature())