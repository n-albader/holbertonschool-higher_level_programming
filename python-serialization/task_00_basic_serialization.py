#!/usr/bin/env python3

import json


def serialize_and_save_to_file(data, filename):
    """" serialize and save data to the specified file"""
    with open(filename, "w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """load and deserialize data from the specified file"""
    with open(filename, "r") as file:
        return json.load(file)
