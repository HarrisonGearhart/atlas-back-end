#!/usr/bin/python3
"""Getting data from API"""


import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.arv[1])).json()
    todos = requests.get(url + "todos?userID={}".format(sys.argv[1])).json()

    completed = [todo.get("title") for todo in todos if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for task in completed:
        print("\t {}".format(task))
