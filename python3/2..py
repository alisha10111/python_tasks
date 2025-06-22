import sqlite3

try:
    # Connect to the SQLite database
    conn = sqlite3.connect('cities.db')
    cursor = conn.cursor()

    # Define the ID to query
    city_id = 1661

    # Execute the SQL query
    cursor.execute("SELECT * FROM CITY WHERE ID = ?", (city_id,))

    # Fetch the result
    city_data = cursor.fetchone()

    # Print the result
    if city_data:
        print(f"City with ID {city_id}:")
        # Assuming the order of columns matches the table description
        print(f"ID: {city_data[0]}")
        print(f"Name: {city_data[1]}")
        print(f"Country Code: {city_data[2]}")
        print(f"District: {city_data[3]}")
        print(f"Population: {city_data[4]}")
    else:
        print(f"No city found with ID {city_id}.")

except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()