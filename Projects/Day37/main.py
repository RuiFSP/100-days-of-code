import os
from datetime import datetime

import requests

USERNAME = "ruipinto"
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"

# create a new user
# 1 POST - /v1/users
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# 2 create graph
# POST - /v1/users/<username>/graphs
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {"X-USER-TOKEN": TOKEN}
graph_config = {
    "id": GRAPH_ID,
    "name": "Programming",
    "unit": "hours",
    "type": "int",
    "color": "shibafu"
}

# 3 creating a data point - pixel
# POST - /v1/users/<username>/graphs/<graphID>
day_to_insert = datetime(2023, 1, 4)
pixel_creating_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": day_to_insert.strftime("%Y%m%d"),
    "quantity": "2",
}

# 4 update a pixel value
# PUT - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

date_to_correct = datetime(2023, 2, 2)
update_pixel_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_correct.strftime('%Y%m%d')}"
pixel_update = {"quantity": "4"}

# 5 delete pixel
# DELETE - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

date_to_delete = datetime(2023, 2, 5)
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete.strftime('%Y%m%d')}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
