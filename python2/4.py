def print_rangoli(size):
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        lines.append(s.center(4*size-3, "-"))
    print('\n'.join(lines[::-1] + lines[1:]))


print_rangoli(3)

