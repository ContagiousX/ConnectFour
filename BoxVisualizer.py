holes = [ [' ' for x in range(7)] for y in range(6)]

for row in range(len(holes)):
    for col in range(len(holes[0])):
        holes[row][col] = row,col

for row in holes:
    print(row)

