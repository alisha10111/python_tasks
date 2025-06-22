import sqlite3

# 1. Connect to a database (or create a new one)
conn = sqlite3.connect('world_data.db')
cursor = conn.cursor()

# 2. Create the CITY table
cursor.execute('''
CREATE TABLE IF NOT EXISTS CITY (
    ID INTEGER PRIMARY KEY,
    NAME VARCHAR(17),
    COUNTRYCODE VARCHAR(3),
    DISTRICT VARCHAR(20),
    POPULATION INTEGER
);
''')

# 3. Create the COUNTRY table
cursor.execute('''
CREATE TABLE IF NOT EXISTS COUNTRY (
    CODE VARCHAR(3) PRIMARY KEY,
    NAME VARCHAR(44),
    CONTINENT VARCHAR(13),
    REGION VARCHAR(25),
    SURFACEAREA REAL,
    INDEPYEAR VARCHAR(5),
    POPULATION INTEGER,
    LIFEEXPECTANCY REAL,
    GNP REAL,
    GNPOLD VARCHAR(9),
    LOCALNAME VARCHAR(44),
    GOVERNMENTFORM VARCHAR(44),
    HEADOFSTATE VARCHAR(32),
    CAPITAL INTEGER,
    CODE2 VARCHAR(2)
);
''')

# 4. Insert sample data (optional, for demonstration)
# Sample data for CITY
city_data = [
    (1, 'New York', 'USA', 'New York', 8000000),
    (2, 'London', 'GBR', 'England', 9000000),
    (3, 'Paris', 'FRA', 'Ile-de-France', 2000000),
    (4, 'Tokyo', 'JPN', 'Tokyo', 14000000),
    (5, 'Cairo', 'EGY', 'Cairo', 9500000),
    (6, 'Berlin', 'DEU', 'Berlin', 3700000),
    (7, 'Mumbai', 'IND', 'Maharashtra', 12500000),
    (8, 'Sydney', 'AUS', 'New South Wales', 5300000)
]
cursor.executemany('INSERT OR IGNORE INTO CITY VALUES (?, ?, ?, ?, ?)', city_data)

# Sample data for COUNTRY
country_data = [
    ('USA', 'United States', 'North America', 'North America', 9834000, '1776', 330000000, 78.5, 21000000, '20000000', 'United States', 'Federal Republic', 'Joe Biden', 1, 'US'),
    ('GBR', 'United Kingdom', 'Europe', 'Western Europe', 243610, '1707', 67000000, 81.0, 3000000, '2900000', 'United Kingdom', 'Constitutional Monarchy', 'Charles III', 2, 'GB'),
    ('FRA', 'France', 'Europe', 'Western Europe', 551695, '843', 65000000, 82.0, 2700000, '2600000', 'France', 'Republic', 'Emmanuel Macron', 3, 'FR'),
    ('JPN', 'Japan', 'Asia', 'Eastern Asia', 377975, '660', 126000000, 84.0, 5000000, '4900000', 'Nippon', 'Constitutional Monarchy', 'Naruhito', 4, 'JP'),
    ('EGY', 'Egypt', 'Africa', 'Northern Africa', 1010408, '1922', 102000000, 72.0, 300000, '290000', 'Misr', 'Republic', 'Abdel Fattah el-Sisi', 5, 'EG'),
    ('DEU', 'Germany', 'Europe', 'Western Europe', 357022, '1871', 83000000, 81.0, 4000000, '3900000', 'Deutschland', 'Federal Republic', 'Frank-Walter Steinmeier', 6, 'DE'),
    ('IND', 'India', 'Asia', 'Southern Asia', 3287590, '1947', 1400000000, 69.0, 3500000, '3400000', 'Bharat', 'Federal Republic', 'Draupadi Murmu', 7, 'IN'),
    ('AUS', 'Australia', 'Oceania', 'Australia and New Zealand', 7692024, '1901', 26000000, 83.0, 1500000, '1400000', 'Australia', 'Constitutional Monarchy', 'Charles III', 8, 'AU')
]
cursor.executemany('INSERT OR IGNORE INTO COUNTRY VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', country_data)

# Commit changes
conn.commit()

# 5. Query the names of all continents and their respective average city populations
query = '''
SELECT
    C.Continent,
    CAST(AVG(T.Population) AS INTEGER) AS AverageCityPopulation
FROM
    CITY AS T
JOIN
    COUNTRY AS C ON T.CountryCode = C.Code
GROUP BY
    C.Continent;
'''

cursor.execute(query)
results = cursor.fetchall()

print("Continent | Average City Population")
print("---------------------------------")
for row in results:
    print(f"{row[0]:<9} | {row[1]}")

# Close the connection
conn.close()