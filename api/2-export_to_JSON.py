#!/usr/bin/python3
"""Getting data from API"""


import requests
import sys
import json


def main():
    """According to user_id, show information
    """
    user_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        user_id)
    name = requests.get(user).json().get('username')
    request_todo = requests.get(todos).json()
    tasks = []

    with open('{}.json'.format(user_id), 'w+') as file:
        for todo in request_todo:
            task = {"task": todo.get("title"),
                    "completed": todo.get("completed", "username": name)}
            tasks.append(task)
        info = {user_id: tasks}
        file.write(json.dumps(info))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
