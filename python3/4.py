import sqlite3

# Connect to a SQLite database
conn = sqlite3.connect('cities.db')
cursor = conn.cursor()

# Create the CITY table

cursor.execute('''
    CREATE TABLE IF NOT EXISTS CITY (
        ID INTEGER PRIMARY KEY,
        NAME TEXT(17),
        COUNTRYCODE TEXT(3),
        DISTRICT TEXT(20),
        POPULATION INTEGER
    )
''')

# Insert some sample data
cursor.execute("INSERT INTO CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES (1, 'Tokyo', 'JPN', 'Kanto', 13960000)")
cursor.execute("INSERT INTO CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES (2, 'Kyoto', 'JPN', 'Kansai', 1475000)")
cursor.execute("INSERT INTO CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES (3, 'New York', 'USA', 'New York', 8419000)")
cursor.execute("INSERT INTO CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES (4, 'Osaka', 'JPN', 'Kansai', 2750000)")
cursor.execute("INSERT INTO CITY (ID, NAME, COUNTRYCODE, DISTRICT, POPULATION) VALUES (5, 'London', 'GBR', 'England', 8982000)")

# Query all attributes of every Japanese city
cursor.execute("SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN'")

# Fetch all the results
japanese_cities = cursor.fetchall()

# Print the results
print("Japanese Cities:")
for city in japanese_cities:
    print(f"ID: {city[0]}, Name: {city[1]}, Country Code: {city[2]}, District: {city[3]}, Population: {city[4]}")

# Commit changes and close the connection
conn.commit()
conn.close()