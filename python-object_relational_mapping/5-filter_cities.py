#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
This script is safe from MySQL injection.
"""

import MySQLdb
import sys


def main():
    """Main function to connect to MySQL and display cities by state"""
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> "
              "<database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Create cursor object
        cursor = db.cursor()

        # Query to get cities for a specific state using parameterized query
        query = ("SELECT cities.name "
                 "FROM cities "
                 "JOIN states ON cities.state_id = states.id "
                 "WHERE states.name = %s "
                 "ORDER BY cities.id ASC")
        cursor.execute(query, (state_name,))

        # Fetch all results
        results = cursor.fetchall()

        # Display results as comma-separated city names
        city_names = [row[0] for row in results]
        print(", ".join(city_names))

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
