#!/usr/bin/python3
"""
This module exports task data to a CSV file.

It fetches tasks for a given user from the JSONPlaceholder API
and writes them to a CSV file.
"""

import csv
import requests
import sys


def fetch_data(user_id):
    """
    Fetch user and task data from JSONPlaceholder API.

    Args:
        user_id (str): The ID of the user to fetch tasks for.

    Returns:
        dict: The user data.
        list: The task data.
    """
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                         format(user_id)).json()
    return user, todos


def write_to_csv(user_id, user, todos):
    """
    Write task data to a CSV file.

    Args:
        user_id (str): The ID of the user.
        user (dict): The user data.
        todos (list): The task data.
    """
    with open('{}.csv'.format(user_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, user['username'],
                            task['completed'], task['title']])


if __name__ == "__main__":
    """
    Main function that fetches data and writes it to a CSV file.
    """
    user_id = sys.argv[1]
    user, todos = fetch_data(user_id)
    write_to_csv(user_id, user, todos)
