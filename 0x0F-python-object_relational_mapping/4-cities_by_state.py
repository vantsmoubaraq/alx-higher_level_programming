#!/usr/bin/python3

'''
Module  lists all cities from the database hbtn_0e_4_usa
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    '''
    Not be executed when imported
    '''
    user = argv[1]
    password = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                           passwd=password, db=db, charset="utf8")
    session = conn.cursor()

    session.execute('SELECT * FROM cities ORDER BY cities.id')

    states = session.fetchall()

    for state in states:
        print(state)

    session.close()
    conn.close()
