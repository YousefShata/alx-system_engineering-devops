#!/usr/bin/python3
"""
Gather data
"""
import requests
import sys
import csv

if __name__ == "__main__":
    ID = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    employeeURL = '{}/users/{}'.format(url, ID)

    res1 = requests.get(employeeURL)

    todoURL = '{}/users/{}/todos'.format(url, ID)

    res2 = requests.get(todoURL)

    done = []

    for task in done:
        print("\t {}".format(task.get("title")))

    filename = '{}.csv'.format(ID)
    username = res1.json().get('username')

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in res2.json():
            condition = task.get('completed')
            title = str(task.get('title'))
            writer.writerow([ID, username, condition, title])
