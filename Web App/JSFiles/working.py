import requests
db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"

path = "level1.json" #This node was created in the Firebase console in step 1

response = requests.get(db+"/temp_&_humidity/.json")
print(type(str(response.json())))