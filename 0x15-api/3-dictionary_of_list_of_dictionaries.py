#!/usr/bin/python3
"""
This module exports task data for all employees to a JSON file.

It fetches tasks for all users from the JSONPlaceholder API
and writes them to a JSON file.
"""

import json
import requests


def fetch_data():
    """
    Fetch user and task data for all users from JSONPlaceholder API.

    Returns:
        dict: A dictionary mapping user IDs to a list of task dictionaries.
    """
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_tasks = {}
    for user in users:
        user_id = user['id']
        tasks = [task for task in todos if task['userId'] == user_id]
        task_list = []
        for task in tasks:
            task_dict = {"username": user['username'],
                         "task": task['title'],
                         "completed": task['completed']}
            task_list.append(task_dict)
        user_tasks[user_id] = task_list

    return user_tasks


def write_to_json(user_tasks):
    """
    Write task data for all users to a JSON file.

    Args:
        user_tasks (dict): A dictionary mapping user IDs
        to a list of task dictionaries.
    """
    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_tasks, file)


if __name__ == "__main__":
    """
    Main function that fetches data and writes it to a JSON file.
    """
    user_tasks = fetch_data()
    write_to_json(user_tasks)
