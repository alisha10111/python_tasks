import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))