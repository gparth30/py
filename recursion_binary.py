def binary(number):
    reminder=number%2
    number=int(number/2)
    if number>0:
        binary(number)
    print(reminder,end=' ')
number=int(input("Enter The Number.:"))
binary(number)