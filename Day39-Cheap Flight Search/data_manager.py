import requests
from pprint import pprint

sheet_endpoint = "https://api.sheety.co/cf9a3ecccb88b5670ee5f611a250b5be/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheet_endpoint)
        data = response.json()
        self.destination_data = data['prices']
        # pprint(data)
        return self.destination_data

    def put_destination_data(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    "iataCode": city['iataCode']
                }
            }
        result = requests.put(url=f"{sheet_endpoint}/{city['id']}",
                              json=new_data)
        print(result.text)

