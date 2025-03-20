#!/usr/bin/python3
"""Returns to-do list information for all employees and exports data to JSON."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    all_tasks = {}
    for i in users:
        user_id = i.get("id")
        username = i.get("username")
        all_tasks[user_id] = []
        
        for j in todos:
            if j.get("userId") == user_id:
                all_tasks[user_id].append({
                    "username": username,
                    "task": j.get("title"),
                    "completed": j.get("completed")
                    })

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(all_tasks, file)
