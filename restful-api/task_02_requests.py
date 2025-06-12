#!/usr/bin/python3
'''
task_02_requests.py
'''
import csv


import requests


def fetch_and_print_posts():

    r = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        post = r.json()
        print("Titles: {}".format(post['title']))


def fetch_and_save_posts():

    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    if r.status_code == 200:
        posts = r.json()
        save_post = []
        for post in posts:
            data_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body'],
            }
            save_post.append(data_post)

        with open("post.csv", "w") as csv_file:
            col = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=col)
            writer.writeheader()
            writer.writerows(save_post)
