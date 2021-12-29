n=int(input("Enter Number Of Raw & Columnn.:"))
k=2
for raw in range (1,n+1):
    for column in range (1,2*n):
        if raw+column==n+1 or column-raw==n-1:
            print("*",end=' ')
        elif raw==n and column!=k:
            print("*",end=' ')
            k=k+2
        else:
            print(" ",end=' ')
    print("")