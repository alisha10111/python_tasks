# Find probability using combinations.
from itertools import combinations

n = int(input())                          # Number of letters
letters = input().split()                # The list of letters
k = int(input())                          # Size of combinations

comb = list(combinations(letters, k))    # All possible k-combinations

# Count combinations containing at least one 'a'
count = sum(1 for c in comb if 'a' in c)

# Print probability rounded to 4 decimal places
print(f"{count / len(comb):.4f}")

