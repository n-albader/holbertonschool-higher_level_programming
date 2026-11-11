#!/usr/bin/env python3

import json
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/items')
def items():
    file_path = os.path.join(os.path.dirname(__file__), 'items.json')

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return render_template('items.html', items=data['items'])


if __name__ == '__main__':
    app.run(debug=True, port=5000)