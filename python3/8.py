from prettytable import PrettyTable

# 1. Create the STATION table and populate it with sample data
station_table = PrettyTable()
station_table.field_names = ["ID", "CITY", "STATE", "LAT_N", "LONG_W"]

# Sample data based on the problem description
cities_data = [
    (1, "DEF", "RJ", 26.9, 74.6),
    (2, "ABC", "DL", 28.7, 77.2),
    (3, "PQRS", "UP", 27.2, 78.0),
    (4, "WXY", "MP", 23.2, 77.4),
    (5, "AB", "RJ", 25.0, 70.0), # Added for a shorter example
    (6, "ABCDE", "DL", 29.0, 75.0), # Added for a longer example
    (7, "PQR", "UP", 27.0, 78.0) # Added for a tie-breaking example
]

for row in cities_data:
    station_table.add_row(row)

print("STATION Table:")
print(station_table)

# 2. Find the city with the shortest name and longest name
city_names = sorted([(city[1], len(city[1])) for city in cities_data], key=lambda x: (x[1], x[0]))

shortest_city_name = city_names[0][0]
shortest_city_length = city_names[0][1]

longest_city_name = city_names[-1][0]
longest_city_length = city_names[-1][1]

print(f"\nShortest City: {shortest_city_name} {shortest_city_length}")
print(f"Longest City: {longest_city_name} {longest_city_length}")