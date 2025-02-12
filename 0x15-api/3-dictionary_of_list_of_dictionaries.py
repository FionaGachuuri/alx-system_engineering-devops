#!/usr/bin/python3
"""
Exports all employees' TODO list progress to a JSON file using a REST API.
"""

import json
import requests

if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{base_url}/users").json()

    all_tasks = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]

        todos = requests.get(f"{base_url}/todos?userId={user_id}").json()

        all_tasks[user_id] = [
            {"task": todo["title"],
             "completed": todo["completed"], "username": username}
            for todo in todos
        ]

    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(all_tasks, file, indent=4)

    print(f"Data exported to {filename}")
