import requests
db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"


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
print(get_TVOC())