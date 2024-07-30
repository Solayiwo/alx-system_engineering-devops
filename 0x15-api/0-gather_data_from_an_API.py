#!/usr/bin/python3
"""A python script that return employee TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    user_api_url = f"{base_url}users/{employee_id}"
    user_reponse = requests.get(user_api_url)
    user_data = user_reponse.json()

    params = {"userId": employee_id}

    todos_api_url = f"{base_url}todos"
    todos_response = requests.get(todos_api_url, params=params)
    todos_data = todos_response.json()

    completed = []
    for task in todos_data:
        if task.get("completed") is True:
            completed.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
            user_data.get("name"), len(completed), len(todos_data)))

    for complete in completed:
        print("\t {}".format(complete))
