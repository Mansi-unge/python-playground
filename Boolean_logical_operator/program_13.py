def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 == 0  and year % 100 != 0) or year % 400 == 0:
        return year
    return leap

year = int(input("enter your year: "))
print(is_leap(year))