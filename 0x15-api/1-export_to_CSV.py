#!/usr/bin/python3
"""A python script that export data (employee TODO list) to CSV format
"""

import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]

    user_api_url = f"{base_url}users/{user_id}"
    user_reponse = requests.get(user_api_url)
    user_data = user_reponse.json()

    username = user_data.get("username")
    params = {"userId": user_id}

    todos_api_url = f"{base_url}todos"
    todos_response = requests.get(todos_api_url, params=params)
    todos_data = todos_response.json()

    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        content = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            content.writerow(
                    [user_id, username,
                        task.get("completed"),
                        task.get("title")]
                    )
