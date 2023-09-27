#!/usr/bin/python3
"""
This module uses the JSONPlaceholder API to get information about an employee's
TODO list progress.

It uses the requests module to make HTTP requests and sys module to read the
command-line argument.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <employee ID>'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to reach the API")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".
          format(user_data.get('name'), len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
