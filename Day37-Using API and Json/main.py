import requests
import json
from datetime import datetime


TOKEN = "shfjkahjdkshfjadk"
USERNAME = "queena"
pixela_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url= pixela_endpoint, json=user_params)
# print(response.text)


post_graph_endpoint = f"{pixela_endpoint}"
graph_config = {
    "id": "graph2",
    "name": "Workout Graph",
    "unit": "Calorie",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN

}


today = datetime.now()
print(today)

# response = requests.post(url=post_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

get_graph_endpoint = f"{pixela_endpoint}/{graph_config['id']}"
# print(get_graph_endpoint)
#"20210322"
data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input(f"How many calories did you burn today?")
}

response = requests.post(get_graph_endpoint, headers=headers, data=json.dumps(data))
print(response.text, response.status_code)

put_graph_endpoint = f"{get_graph_endpoint}/{data['date']}"
put_data = {
    "quantity": "250",
    "optionalData": "{\"Exercise\":\"HIIT\"}"
}
# response = requests.put(put_graph_endpoint, headers=headers,data=json.dumps(put_data))
# print(response.status_code, response.text, get_graph_endpoint+".html")

delete_graph_endpoint = f"{put_graph_endpoint}"
# response = requests.delete(delete_graph_endpoint,headers=headers)
# print(response.text, response.status_code, get_graph_endpoint+".html")