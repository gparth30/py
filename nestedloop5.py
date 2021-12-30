n=int(input("Enter the Number Of Raws.:"))

for raw in range(n):
    for column in range (n-raw):
        print(column+1,end=' ')
    print("")