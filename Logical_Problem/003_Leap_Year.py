# Determine if a year is a Leap Year

# Description: A year is a Leap Year if it is divisible by 400, or divisible by 4 but not by 100

a = int(input("Enter the Year : "))

if (a%400==0) or (a%4==0 and a%100!=0):
    print(f"{a} is a Leap Year")
else:
    print(f"{a} is not a Leap Year")