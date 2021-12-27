'''
1 2 1 2 1
1 2 1 2 
1 2 1
1 2
1 
'''
row = 5
while row >= 1:
    column = 1
    while column <= row:
        if column % 2 == 0:
            print("2", end=' ')
        else:
            print("1", end=' ')
        column = column+1
    print("")
    row = row-1