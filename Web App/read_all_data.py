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

def get_pressure():
        response = requests.get(db+"/Pressure.json")
        pressure = response.json()
        pressure_list = list(pressure.values())
        k=0
        sum=0
        while (k<len(pressure_list)):
            p = pressure_list[k]
            p1 = p["Pressure"]
            sum = sum + p1
            k+=1
        avg = sum/k
        return round(avg, 1)

def get_temperature():
        response = requests.get(db+"/Temperature.json")
        temperature = response.json()
        temp_list = list(temperature.values())
        k=0
        sum=0
        while (k<len(temp_list)):
            p = temp_list[k]
            p1 = p["Temperature"]
            sum = sum + p1
            k+=1
        avg = sum/k
        return round(avg, 1)

def get_TVOC():
        response = requests.get(db+"/TVOC.json")
        TVOC = response.json()
        TVOC_list = list(TVOC.values())
        k=0
        sum=0
        while (k<len(TVOC_list)):
            p = TVOC_list[k]
            p1 = p["TVOC"]
            sum = sum + p1
            k+=1
        avg = sum/k
        return round(avg, 1)