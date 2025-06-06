#  Convert list to tuple and print its hash.
n = int(input())
integer_list = map(int, input().split())
print(hash(tuple(integer_list)))
