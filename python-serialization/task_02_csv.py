#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV data to JSON and save it to data.json"""
    try:
        with open(filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True

    except FileNotFoundError:
        return False
