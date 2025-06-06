# Vowel vs consonant substring game. Count scores.
from itertools import groupby
s = input()
print(' '.join(f"({len(list(g))}, {k})" for k, g in groupby(s)))