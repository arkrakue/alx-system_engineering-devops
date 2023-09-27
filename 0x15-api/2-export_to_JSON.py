#!/usr/bin/python3
"""
This module exports task data to a JSON file.

It fetches tasks for a given user from the JSONPlaceholder API
and writes them to a JSON file.
"""

import json
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


def write_to_json(user_id, user, todos):
    """
    Write task data to a JSON file.

    Args:
        user_id (str): The ID of the user.
        user (dict): The user data.
        todos (list): The task data.
    """
    tasks = []
    for task in todos:
        task_dict = {"task": task['title'],
                     "completed": task['completed'],
                     "username": user['username']}
        tasks.append(task_dict)

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump({user_id: tasks}, file)


if __name__ == "__main__":
    """
    Main function that fetches data and writes it to a JSON file.
    """
    user_id = sys.argv[1]
    user, todos = fetch_data(user_id)
    write_to_json(user_id, user, todos)
