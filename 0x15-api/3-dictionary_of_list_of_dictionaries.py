#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    id_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(id_url + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            pop.get("id"): [{
                "task": lop.get("title"),
                "completed": lop.get("completed"),
                "username": pop.get("username")
            } for lop in requests.get(id_url + "todos",
                                      params={"userId": pop.get("id")}).json()]
            for pop in employee}, f)
