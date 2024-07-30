#!/usr/bin/python3
"""A python script that export data (all employee TODO list) to JSON format"""

import json
import requests


def get_user_data():
    """Fetch usser information and to-do lists for all employees."""
    base_url = "https://jsonplaceholder.typicode.com/"
    user_api_url = f"{base_url}users"
    user_reponse = requests.get(user_api_url)
    user_data = user_reponse.json()

    export_data = {}

    for user in user_data:
        user_id = user["id"]

        todos_api_url = f"{base_url}todos"
        todos_response = requests.get(todos_api_url)
        todos_data = todos_response.json()

        export_data[user_id] = []

        for task in todos_data:
            task_details = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            }
            export_data[user_id].append(task_details)
    return export_data


if __name__ == "__main__":
    export_data = get_user_data()
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(export_data, json_file, indent=2)
