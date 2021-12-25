#write a program to print following series (Lucas series)
#2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 .... 300

previous=2
current=1
print(f"{previous} {current}",end=' ')
while current<199:
    next=previous+current
    print(f"{next}",end=' ')
    previous=current
    current=next
    


