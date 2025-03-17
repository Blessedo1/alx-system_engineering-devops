#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = 0
    for i in todos:
        if i.get("completed") is True:
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), completed, len(todos)))
    for i in todos:
        if i.get("completed") is True:
            print("\t {}".format(i.get("title")))
