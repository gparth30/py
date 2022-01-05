def factorial(number):
    factorial=1
    while number>=1:
        factorial=factorial*number
        number=number-1
    print(factorial)    

number=int(input("Enter The Number.:"))
factorial(number)

