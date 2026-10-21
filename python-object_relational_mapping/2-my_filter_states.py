#!/usr/bin/python3
"""Lists states matching a name provided by the user"""

import MySQLdb
import sys


if __name__ == "__main__":
    """Displays states matching the given name in ascending ID order"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(
            sys.argv[4]
    )
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
