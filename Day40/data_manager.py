import requests

sheety_endpoint = "https://api.sheety.co/cf9a3ecccb88b5670ee5f611a250b5be/flightDeals/users"

def get_customer_emails():
    customers_endpoint = sheety_endpoint
    response = requests.get(customers_endpoint)
    data = response.json()
    customer_data = data["users"]
    print(customer_data)
    return customer_data


def add_customer_emails():
    customers_endpoint = sheety_endpoint
    fname = input("Whats your first name?")
    lname = input("Whats your last name?")
    email = input("Whats your email?")
    row = {'firstName': fname, 'lastName': lname, 'email': email, 'id': 2}
    customer_data = {'users': row}
    print(customer_data)
    response = requests.post(customers_endpoint, data={'users': customer_data})
    print(dir(response ))
    print("Status Code: ", response.status_code, "\nReason: ", response.reason)


add_customer_emails()
