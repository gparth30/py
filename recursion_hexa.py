def hexa(number):
    reminder=number%16
    number=int(number/16)
    if number>0:
        hexa(number)
    if reminder<10:
        print(reminder,end=' ')
    elif reminder==10:
        print("A",end=' ')
    elif reminder==11:
        print("B",end=' ')
    elif reminder==12:
        print("C",end=' ')
    elif reminder==13:
        print("D",end=' ')
    elif reminder==14:
        print("E",end=' ')
    elif reminder==15:
        print("F",end=' ')
number=int(input("Enter The Number.:"))
hexa(number)