import sqlite3

# Connect to a SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('city_database.db')
cursor = conn.cursor()

# Create the CITY table
cursor.execute('''
CREATE TABLE IF NOT EXISTS CITY (
    ID INTEGER PRIMARY KEY,
    NAME VARCHAR(17),
    COUNTRYCODE VARCHAR(3),
    DISTRICT VARCHAR(20),
    POPULATION INTEGER
)
''')

# Insert some sample data (optional, for demonstration)
cursor.execute("INSERT INTO CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES (1, 'New York', 'USA', 'New York', 8000000)")
cursor.execute("INSERT INTO CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES (2, 'London', 'GBR', 'Greater London', 9000000)")
cursor.execute("INSERT INTO CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES (3, 'Paris', 'FRA', 'Ile-de-France', 2100000)")
cursor.execute("INSERT INTO CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES (4, 'Tokyo', 'JPN', 'Tokyo', 14000000)")

# Query the average population, rounded down to the nearest integer
cursor.execute("SELECT CAST(AVG(POPULATION) AS INTEGER) FROM CITY")
average_population = cursor.fetchone()[0]

# Print the result
print(f"The average population for all cities is: {average_population}")

# Commit changes and close the connection
conn.commit()
conn.close()