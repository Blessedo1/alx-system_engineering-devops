#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    username = user.get("username")

    with open("{}.csv".format(sys.argv[1]), mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in todos:
            writer.writerow([sys.argv[1], username, i.get("completed"), i.get("title")])

    completed = 0
    for i in todos:
        if i.get("completed") is True:
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), completed, len(todos)))
    for i in todos:
        if i.get("completed") is True:
            print("\t {}".format(i.get("title")))
