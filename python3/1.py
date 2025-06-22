import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the CITY table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS CITY (
        ID NUMBER,
        NAME VARCHAR2(17),
        COUNTRYCODE VARCHAR2(3),
        DISTRICT VARCHAR2(20),
        POPULATION NUMBER
    );
''')

# Insert some sample data
cursor.execute("INSERT INTO CITY VALUES (1, 'New York', 'USA', 'New York', 8000000);")
cursor.execute("INSERT INTO CITY VALUES (2, 'London', 'UKG', 'England', 9000000);")
conn.commit()

# Query all columns for every row in the CITY table
cursor.execute("SELECT * FROM CITY;")

# Fetch all the results
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()