#!/usr/bin/python3
"""Lists all states from a MySQL database"""


import MySQLdb
import sys


def main():
    """Connects to MySQL and displays all states ordered by ID"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()

