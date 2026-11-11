#!/usr/bin/env python3

import csv
import json
import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_json():
    """Read products from the JSON file."""
    file_path = os.path.join(BASE_DIR, 'products.json')

    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv():
    """Read products from the CSV file."""
    file_path = os.path.join(BASE_DIR, 'products.csv')

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        products = []

        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

        return products


def read_sql():
    """Read products from the SQLite database."""
    db_path = os.path.join(BASE_DIR, 'products.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, name, category, price FROM Products'
        )
        products = [dict(row) for row in cursor.fetchall()]
        return products
    finally:
        conn.close()


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQLite."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            products_list = read_json()
        elif source == 'csv':
            products_list = read_csv()
        elif source == 'sql':
            products_list = read_sql()
        else:
            return render_template(
                'product_display.html',
                products=[],
                error='Wrong source'
            )

        if product_id is not None:
            products_list = [
                product for product in products_list
                if str(product['id']) == product_id
            ]

            if not products_list:
                return render_template(
                    'product_display.html',
                    products=[],
                    error='Product not found'
                )

        return render_template(
            'product_display.html',
            products=products_list,
            error=None
        )

    except sqlite3.Error:
        return render_template(
            'product_display.html',
            products=[],
            error='Database error'
        )


if __name__ == '__main__':
    app.run(debug=True, port=5000)