import sqlite3

db = sqlite3.connect('my_first_db.db')  # Creates or opens a databsase file

cur = db.cursor()  # Need a cursor object to perform operations

# Create a table
cur.execute('create table if not exists phones (brand text, version int)')

# # Add some data
# cur.execute('insert into phones values ("Android", 5)')
# cur.execute('insert into phones values ("iPhone", 6)')
#

# Ask user for information for a new phone
brand = input('Enter brand of phone: ')
version = int(input('Enter version of phone (as an integer): '))

# Parameters. Use a ? as a placeholder for data that will be filled in
# Provide data as a second argument to .execute, as a tuple of values
cur.execute('insert into phones values (?, ?)', (brand, version))

# # Execute a query. Results are contained in cursor object
# for row in cur.execute('select * from phones'):
#     print(row)
#

# Execute a query. Results are contained in cursor object
results = cur.execute("select * from phones")
for row in results:
    print(row)

# cur.execute('drop table phones')  # Delete table
#
db.commit()  # Ask the database to save changes

db.close()