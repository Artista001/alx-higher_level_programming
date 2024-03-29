#!/usr/bin/python3
"""
This script takes in an argument and
displays all the values in the states table of
hbtn_0e_0_usa wher the name 
matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Access to the database
    and retrieve the required
    data.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         port=3306, passwd=argv[2], db=argv[3])
    with db.cursor() as cur:
        cur.execute("""
             SELECT
                  *
              FROM
                  states
              WHERE
                   name like BINARY %(name)s
              ORDER BY
                  states.id ASC
        """, {
              'name': argv[4]
        })

        rows = cur.fetchall()
    if rows is not None:
          for row in rows:
             print(row)
