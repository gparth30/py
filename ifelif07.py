'''
write a program to findout whether given year is leap year or not 
https://www.wikihow.com/Calculate-Leap-Years
'''

year=int(input("Enetr Year.:"))


if year%100==0:
    print(f"{year}, is Leap Year")
elif year%400==0:
    print(f"{year}, is Leap Year")
elif year%4==0:
    print(f"{year}, is Leap Year")
else:
    print(f"{year}, is Not Leap year")