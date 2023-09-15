#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                        password=argv[2], db=argv[3], searched=argv[4], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY searched ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
            print(row)
    cur.close()
    db.close()
