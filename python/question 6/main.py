#Count word frequencies in input order.
from collections import OrderedDict

n = int(input())
counts = OrderedDict()

for _ in range(n):
    word = input()
    counts[word] = counts.get(word, 0) + 1

print(len(counts))
print(*counts.values())
