import pandas as pd


data = {
    'employee_id': [12228, 33645, 45692, 56118, 59725, 74197, 78454, 83565, 98607, 99989],
    'name': ['Rose', 'Angela', 'Frank', 'Patrick', 'Lisa', 'Kimberly', 'Bonnie', 'Michael', 'Todd', 'Joe'],
    'months': [15, 1, 17, 7, 11, 16, 8, 6, 5, 9],
    'salary': [1968, 3443, 1608, 1345, 2330, 4372, 1771, 2017, 3396, 3573]
}
employee_df = pd.DataFrame(data)

# Sort the DataFrame by the 'name' column in alphabetical order
sorted_employees = employee_df.sort_values(by='name')

# Print the sorted employee names
print(sorted_employees['name'].tolist())