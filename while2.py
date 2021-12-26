#write a program to print following series (triangular numbers)
#0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ... 1000

number=0
while number<45:
    add=int(number*(number+1)*.5)
    print(add,end=' ')
    number=number+1