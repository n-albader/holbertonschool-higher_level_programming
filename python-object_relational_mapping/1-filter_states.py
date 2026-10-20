#!/usr/bin/python3
"""Lists states whose names start with N."""

import MySQLdb
import sys


def main():
    """Displays states starting with uppercase N."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
