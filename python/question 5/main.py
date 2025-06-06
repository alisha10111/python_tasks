#Write a function to check for leap year
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter year: "))
print(is_leap(year))
