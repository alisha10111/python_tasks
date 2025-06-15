from collections import Counter

x = int(input())
sizes = Counter(map(int, input().split()))
n = int(input())
total = 0

for _ in range(n):
    size, price = map(int, input().split())
    if sizes[size]:
        total += price
        sizes[size] -= 1

print(total)
