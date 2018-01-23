import sqlite3

db = sqlite3.connect('my_first_db.db')  # Creates or opens a databsase file

cur = db.cursor()  # Need a cursor object to perform operations

# Create a table
cur.execute('create table if not exists chainsaw_juggling_records (name text, country text, catches)')


# confirm returns true if user's answer to a question is yes.
def confirm(question):
    return input(question).lower().startswith('y')


# Ask user for information to add a record
def new_data():
    name = input('Enter name of record holder: \n')
    country = input('Enter Country of participation: \n')
    catches = int(input('Enter number of catches: \n'))

    # Parameters with ? as placeholders and data as second argument to .execute as a tuple of values.
    cur.execute('insert into chainsaw_juggling_records values (?, ?, ?)', (name, country, catches))

# Ask user if they would like to search for a specific record
if confirm('Would you like to search for a specific record? \n'):
    search_term = input('Please enter a name to look for: \n')
    results = cur.execute("select * from chainsaw_juggling_records where name = ?", (search_term, ))
    for row in results:
        print(row)
    if confirm('Would you like to delete or modify this entry? \n'):
        if confirm('Would you like to modify this entry? \n'):
            new_record = input('What is the new record for this entry? \n')
            cur.execute("update chainsaw_juggling_records set catches=? where name=?", (new_record, search_term, ))
        elif confirm('Would you like to delete this entry? \n'):
            cur.execute("delete from chainsaw_juggling_records where name = ?", (search_term, ))

# Ask if user would like to read data.
if confirm('Would you like to review all data? \n'):
    if confirm('If there is a lot of data, this could take some time or be difficult to review. Are you sure? \n'):
        results = cur.execute("select * from chainsaw_juggling_records")
        for row in results:
            print(row)

# Ask if they would like to add data. If so, get data.
if confirm('Would you like to add a new record? \n'):
    new_data()
    db.commit()

# todo make sure commiting
# Ask if user would like to delete data
