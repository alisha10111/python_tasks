def solve(s):
    return ' '.join(word.capitalize() for word in s.split())

# Example
print(solve("hello world"))
