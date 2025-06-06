#!/usr/bin/env python3
'''
task_02_csv.py
'''


import csv
import json


def convert_csv_to_json(CSV):
    try:
        with open(CSV, 'w') as c_file:
            read = csv.DictReader(CSV)
            data = list(read)

        with open("data.json", 'w') as j_file:
            json.dumps(data, j_file)

        return (True)
    except FileNotFoundError:
        return(False)
    except Exception:
        return (False)
