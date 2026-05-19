# testing

import requests


# API endpoint
url = "http://127.0.0.1:5000/generate-quote"


# project data to send
project_data = {

    "client_name": "Sokha",
    "project_type": "residential",
    "project_size": "medium",
    "service_category": "home renovation",
    "estimated_budget": "$20,000"

}


# send POST request
response = requests.post(url, json=project_data)


# convert response into JSON
quote_result = response.json()


# display response
print("QuoteBuild API Response")
print("-------------------------")

print("Client Name:", quote_result["client_name"])
print("Project Type:", quote_result["project_type"])
print("Project Size:", quote_result["project_size"])
print("Estimated Price:", quote_result["estimated_price"])
print("Status:", quote_result["status"])
print("Notes:", quote_result["notes"])