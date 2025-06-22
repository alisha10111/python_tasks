import sqlite3

# Connect to a SQLite database
conn = sqlite3.connect('station.db')
cursor = conn.cursor()

# Create the STATION table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS STATION (
        ID NUMBER,
        CITY VARCHAR2(21),
        STATE VARCHAR2(2),
        LAT_N NUMBER,
        LONG_W NUMBER
    )
''')

# Insert some sample data
cursor.execute("INSERT INTO STATION (ID, CITY, STATE, LAT_N, LONG_W) VALUES (1, 'New York', 'NY', 40.7128, 74.0060)")
cursor.execute("INSERT INTO STATION (ID, CITY, STATE, LAT_N, LONG_W) VALUES (2, 'Los Angeles', 'CA', 34.0522, 118.2437)")
cursor.execute("INSERT INTO STATION (ID, CITY, STATE, LAT_N, LONG_W) VALUES (3, 'Chicago', 'IL', 41.8781, 87.6298)")

# Query a list of CITY and STATE from the STATION table
cursor.execute("SELECT CITY, STATE FROM STATION")
results = cursor.fetchall()

# Print the results
print("CITY and STATE from STATION table:")
for row in results:
    print(f"City: {row[0]}, State: {row[1]}")

# Commit changes and close the connection
conn.commit()
conn.close()