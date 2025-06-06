#Use if-elif-else to check and print conditions (Weird / Not Weird)
n = int(input())
if n % 2 != 0 or (6 <= n <= 20):
    print("Weird")
else:
    print("Not Weird")
