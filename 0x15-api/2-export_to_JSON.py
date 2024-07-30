#!/usr/bin/python3
"""A python script that export data (employee TODO list) to JSON format"""

import json
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

    export_data = {user_id: []}

    for task in todos_data:
        task_details = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        export_data[user_id].append(task_details)

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(export_data, json_file, indent=2)
