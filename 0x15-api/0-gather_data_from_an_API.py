#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    for i in todos:
        completed = 0
        if i.get("completed") is True:
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), completed, len(todos)))
    for i in todos:
        if i.get("completed") is True:
            print("\t {}".format(i.get("title")))
