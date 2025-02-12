#!/usr/bin/python3
"""
This module retrieves and displays an employee's
TODO list progress using a REST API
"""
import requests
import sys


def fetch_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user_url = f"{base_url}users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: User not found")
        return
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch user's TODO list
    todos_url = f"{base_url}todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODO list")
        return
    todos_data = todos_response.json()

    # Calculate completed tasks
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    # Display results
    print(f"Employee {employee_name} is done with tasks
          ({done_tasks}/{total_tasks}): ")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        fetch_todo_progress(int(sys.argv[1]))
