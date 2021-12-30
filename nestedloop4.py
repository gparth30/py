n=int(input("Enter the Number Of Raws.:"))

for raw in range(1,n+1):
    for column in range (1,raw+1):
        if column%2==0:
            print("2",end=' ')
        else:
            print("1",end=' ')
    print("")