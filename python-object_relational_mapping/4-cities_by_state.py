#!/usr/bin/python3
"""Lists all cities with their corresponding states"""

import MySQLdb
import sys


def main():
    """Displays cities and their states in ascending city ID order"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    for city in cursor.fetchall():
        print(city)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
