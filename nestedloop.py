row=int(input("enter Number Of Rows & Column.:"))
for i in range (row,0,-1):
    for j in range (i,0,-1):
        if i==1 or i==row or j==1 or j==i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print("")