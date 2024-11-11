#!/usr/bin/python3
"""Getting data from API"""


import requests
import sys


def main():
    """According to user_id, show information
    """
    user_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        user_id)
    name = requests.get(user).json().get('name')
    request_todo = requests.get(todos).json()
    tasks = [task.get('title')
             for task in request_todo if task.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'.format(name,
                                                          len(tasks),
                                                          len(request_todo)))
    print('\n'.join('\t {}'.format(task) for task in tasks))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()