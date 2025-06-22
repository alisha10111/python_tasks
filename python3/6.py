import sqlite3

station_data = [
    {"ID": 1, "CITY": "New York", "STATE": "NY", "LAT_N": 40.71, "LONG_W": 74.01},
    {"ID": 2, "CITY": "Los Angeles", "STATE": "CA", "LAT_N": 34.05, "LONG_W": 118.24},
    {"ID": 3, "CITY": "Chicago", "STATE": "IL", "LAT_N": 41.88, "LONG_W": 87.63},
    {"ID": 4, "CITY": "Houston", "STATE": "TX", "LAT_N": 29.76, "LONG_W": 95.37},
    {"ID": 5, "CITY": "Phoenix", "STATE": "AZ", "LAT_N": 33.45, "LONG_W": 112.07},
    {"ID": 6, "CITY": "Philadelphia", "STATE": "PA", "LAT_N": 39.95, "LONG_W": 75.17},
    {"ID": 7, "CITY": "New York", "STATE": "NY", "LAT_N": 40.71, "LONG_W": 74.01}, # Duplicate city
    {"ID": 8, "CITY": "San Antonio", "STATE": "TX", "LAT_N": 29.42, "LONG_W": 98.49},
]

# Filter for cities with even ID numbers and collect unique city names
even_id_cities = set()
for record in station_data:
    if record["ID"] % 2 == 0:
        even_id_cities.add(record["CITY"])

# Print the results
print("Cities with even ID numbers (unique):")
for city in sorted(list(even_id_cities)): # Sorted for consistent output, though not required by problem
    print(city)