def octal(number):
    reminder=number%8
    number=int(number/8)
    if number>0:
        octal(number)
    print(reminder,end=' ')
number=int(input("Enter The Number.:"))
octal(number)