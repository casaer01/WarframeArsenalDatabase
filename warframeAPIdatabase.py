import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

parameters = {
    "name": "Amprex"
}

response = requests.get("https://api.warframestat.us/weapons")
todos = json.loads(response.text)

# prints everything of the first item
# print(todos[0])

# Gets name of the first item in the json list
print(todos[0]["name"])


# Prints everything
# jprint(response.json())
# print(response.json())