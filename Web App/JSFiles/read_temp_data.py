import requests
db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"

response1 = requests.get(db+"/temp/.json")
b = response1.json()
b1 = list(b.values())
i=0
while (i<len(b1)):
    s = b1[i]
    s1 = s["Temperature: "]
    i+=1
    print(s1)

response2 = requests.get(db+"/humidity/.json")
c = response2.json()
c1 = list(c.values())
j=0
while (j<len(c1)):
    d = c1[j]
    d1 = d["Humidity: "]
    print(d1)
    j+=1