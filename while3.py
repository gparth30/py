#write a program to print following series (pentagonal  number)
#1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176 ... 300

number=1
while number<15:
    add=int((number-1)*number + number*(number+1)/2)
    print(add,end=' ')
    number=number+1