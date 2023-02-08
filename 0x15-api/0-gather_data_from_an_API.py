#!/usr/bin/python3
""" Getting data from an API
"""

import requests
from sys import argv

if __name__ == '__main__':
    endpoint = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(endpoint + "user/{}".
                        format(user_id)).json()
    todo = requests.get(endpoint + "todos?user_id={}".
                        format(user_id)).json()
    completed_task = []
    for task in todo:
        if task.get('completed') is True:
            completed_task.append(task.get('title'))
    print("Employee {} is done with task({}/{}):".
            format(user.get('name'), len(completed_task), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_task))
