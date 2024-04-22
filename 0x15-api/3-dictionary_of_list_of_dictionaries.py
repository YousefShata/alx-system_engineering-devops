#!/usr/bin/python3
"""
Gather data
"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    employeeURL = '{}/users'.format(url)

    filename = 'todo_all_employees.json'

    res1 = requests.get(employeeURL)

    users = {}
    for records in res1.json():
        users.update({records.get('id'): records.get('username')})

    data = {}
    for key, value in users.items():
        todoURL = '{}/users/{}/todos'.format(url, key)

        res2 = requests.get(todoURL)

        all_tasks = []

        for task in res2.json():
            tasks = {
                "username": value,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            all_tasks.append(tasks)

        data.update({key: all_tasks})

    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)
