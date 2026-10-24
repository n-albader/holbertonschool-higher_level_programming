#!/usr/bin/python3
"""Fetch posts from an API and save them to a CSV file"""

import csv
import requests


def fetch_and_print_posts():
    """Fetch posts and print their titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save selected fields to posts.csv"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        posts_list = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(posts_list)