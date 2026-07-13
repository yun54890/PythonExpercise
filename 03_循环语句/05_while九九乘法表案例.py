

row = 1
while row <= 9:
    col = 1
    while col <= row:

        print(f"{col}*{row}={row*col}",end='\t')
        col += 1
    print("")
    row += 1