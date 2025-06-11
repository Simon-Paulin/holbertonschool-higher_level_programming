#!/usr/bin/python3
'''
task_02_requests.py
'''

import requests
import csv

def fetch_and_print_posts():

    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
            posts = r.json()
            for post in posts:
                print("Titles: {}".format(post['title']))

def fetch_and_save_post():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    if r.status_code == 200:
        posts = r.json()
        save_post = []
        for post in posts:
            data_post = {
                'id': post['id'],
                'titel': post['titel'],
                'body': post['body'],
            }
            save_post.append(data_post)
        with open("post.csv", "w") as csv_file:
            col = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=col)
            writer.writeheader()
            writer.writerows(save_post)
 