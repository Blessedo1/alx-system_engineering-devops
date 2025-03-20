#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    username = user.get("username")
    user_id = sys.argv[1]

    with open("{}.csv".format(user_id), mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in todos:
            writer.writerow(
                    [user_id, username, i.get("completed"), i.get("title")]
                    )

    json_data = {user_id: []}
    for i in todos:
        json_data[user_id].append({
            "task": i.get("title"),
            "completed": i.get("completed"),
            "username": username
            })

    with open("{}.json".format(user_id), mode='w') as file:
        json.dump(json_data, file)

    completed = 0
    for i in todos:
        if i.get("completed") is True:
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), completed, len(todos)))
    for i in todos:
        if i.get("completed") is True:
            print("\t {}".format(i.get("title")))
