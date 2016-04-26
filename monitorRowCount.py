#!/usr/bin/env python

import pymysql.cursors
import pymysql
from optparse import OptionParser


def main():
    parser = OptionParser(usage="usage: %prog -h <host> -u <user> -p <password> -d <database> -t <table> -w <warn> -c <crit>",
    version="%prog 1.0")

    parser.add_option("-H", "--host",
    	action="store",
    	type="string",
    	dest="host",
    	help="host",
    	metavar="HOST")
    parser.add_option("-u", "--user",
    	action="store", type="string",
    	dest="user",
    	help="database username",
    	metavar="USER")
    parser.add_option("-p", "--password",
    	action="store",
    	type="string",
    	dest="pass",
    	help="database password",
    	metavar="PASS")
    parser.add_option("-d", "--database",
    	action="store",
    	type="string",
    	dest="db",
    	help="database name",
    	metavar="DB")
    parser.add_option("-t", "--table",
    	action="store",
    	type="string",
    	dest="table",
    	help="table name",
    	metavar="TABLE")
    parser.add_option("-w", "--warning",
        action="store",
        type="int",
        dest="warning",
        help="warning level",
        metavar="WARNING")
    parser.add_option("-c", "--critical",
        action="store",
        type="int",
        dest="critical",
        help="critical level",
        metavar="CRITICAL")
    (options, args) = parser.parse_args()

    # Connect to the database
    connection = pymysql.connect(host=options.host,
    user=options.user,
    password=options.user,
    db=options.db,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT COUNT(*) FROM " + options.table
            cursor.execute(sql)
            result = cursor.fetchone()
    finally:
        connection.close()

    rows = result['COUNT(*)']

    if rows >= options.critical:
    	print "CRITICAL: " + str(rows)	
    elif rows >= options.warning:
    	print "WARNING: " + str(rows)
    else:
    	print "OK: " + str(rows)

if __name__ == '__main__':
    main()
