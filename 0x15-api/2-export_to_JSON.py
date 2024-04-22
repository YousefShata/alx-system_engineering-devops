#!/usr/bin/python3
"""
Gather data
"""
import json
import requests
import sys

if __name__ == "__main__":
    ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    employeeURL = '{}/users/{}'.format(url, ID)

    res1 = requests.get(employeeURL)

    todoURL = '{}/users/{}/todos'.format(url, ID)

    res2 = requests.get(todoURL)

    filename = '{}.json'.format(ID)
    username = res1.json().get('username')

    all_tasks = []

    for task in res2.json():
        tasks = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        all_tasks.append(tasks)

    data = {
            ID: all_tasks
    }

    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)
