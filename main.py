import sqlite3

# Connect to the database
connection = sqlite3.connect('mydatabase.db')

# Create a cursor object
cursor = connection.cursor()

# Create the books table (if it doesn't exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER
)
''')
# Query data from the table
result = connection.execute("SELECT * FROM books")
data = result.fetchall()

# Process the retrieved data
for row in data:
    print(row)



# Insert the book data
books_data = [("The One and Only Ivan", "Katherine Applegate", 2012)]
cursor.executemany("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", books_data)

# Commit the transaction
connection.commit()

# Close the connection
connection.close()
