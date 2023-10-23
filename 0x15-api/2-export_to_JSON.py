#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    id_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(id_url + "users/{}".format(sys.argv[1])).json()
    t = requests.get(id_url + "todos", params={"userId": sys.argv[1]}).json()
    u = employee.get("username")

    with open("{}.json".format(sys.argv[1]), "w") as f:
        json.dump({sys.argv[1]: [{
                "task": pop.get("title"),
                "completed": pop.get("completed"),
                "username": u
            } for pop in t]}, f)
