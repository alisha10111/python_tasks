import sqlite3

# Connect to an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create the STATION table
cursor.execute('''
    CREATE TABLE STATION (
        ID INTEGER,
        CITY TEXT,
        STATE TEXT,
        LAT_N REAL,
        LONG_W REAL
    )
''')

# Insert sample data
sample_data = [
    (1, 'New York', 'NY', 40.71, -74.00),
    (2, 'New York', 'NY', 40.71, -74.00),
    (3, 'Bengalaru', 'KA', 12.97, 77.59),
    (4, 'London', 'UK', 51.50, -0.12),
    (5, 'London', 'UK', 51.50, -0.12),
    (6, 'Paris', 'FR', 48.85, 2.35)
]
cursor.executemany('INSERT INTO STATION VALUES (?, ?, ?, ?, ?)', sample_data)
conn.commit()

# Calculate total number of city entries
cursor.execute('SELECT COUNT(CITY) FROM STATION')
total_cities = cursor.fetchone()[0]

# Calculate number of distinct city entries
cursor.execute('SELECT COUNT(DISTINCT CITY) FROM STATION')
distinct_cities = cursor.fetchone()[0]

# Calculate difference
difference = total_cities - distinct_cities

# Display results
print(f"Total city entries: {total_cities}")
print(f"Distinct city entries: {distinct_cities}")
print(f"Difference: {difference}")
