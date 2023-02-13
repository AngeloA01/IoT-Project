import requests
db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"

response1 = requests.get(db+"/temperature/.json")
b = response1.json()
b1 = list(b.values())
i=0
while (i<len(b1)):
    s = b1[i]
    s1 = s["temperature: "]
    i+=1
    # print(s1)

response2 = requests.get(db+"/humidity/.json")
c = response2.json()
c1 = list(c.values())
j=0
while (j<len(c1)):
    d = c1[j]
    d1 = d["Humidity: "]
    # print(d1)
    j+=1

    def get_temperature():
        response3 = requests.get(db+"/temperature/.json")
        temperature = response3.json()
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