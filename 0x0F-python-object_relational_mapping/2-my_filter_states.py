#!/usr/bin/python3
"""
This script takes in argument
and displays all values
in the states table of
'hbtn_0e_0_usa where
name mathche argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Access to the database and get
    the required data.
    """

    dtb = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2],
                          db=argv[3])

    cur = dtb.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
