#!/usr/bin/env python3
'''
task_02_csv.py
'''


import csv
import json


def convert_csv_to_json(CSV):
    try:
        with open(CSV, 'r') as c_file:
            read = csv.DictReader(c_file)
            data = list(read)

        with open("data.json", 'w') as j_file:
            json.dump(data, j_file)

        return (True)
    except FileNotFoundError:
        return(False)
    except Exception:
        return (False)
