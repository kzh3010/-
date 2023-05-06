n = int(input())
go = list(input().split())

start_x, start_y = 1, 1

dx = [0,1,0,-1]
dy = [-1,0,1,0]
move = ["L","D","R","U"]

for go in go:
    for i in range(len(move)):
        if go == move[i]:
            go_x = start_x + dx[i]
            go_y = start_y + dy[i]
    if go_x < 1 or go_x > n or go_y < 1 or go_y > n:
        continue
    start_x, start_y = go_x, go_y 

print(start_x, start_y)