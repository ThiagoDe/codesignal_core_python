# field = [[False, True, True],
#          [True, False, True],
#          [False, False, True]]
# x = 1
# y = 1
from collections import deque
import queue


field = [[True, False, True, True, False],
         [True, False, False, False, False],
         [False, False, False, False, False],
         [True, False, False, False, False]]
x = 3
y = 2
# solution(field, x, y) = [[-1, -1, -1, -1, -1],
#                          [-1, 3, 2, 2, 1],
#                          [-1, 2, 0, 0, 0],
#                          [-1, 1, 0, 0, 0]]

def solution(field, x, y):
    num_around = count_bomb(field, x, y)
    if num_around == 0:
        bf(field, x, y)
        
    if num_around > 0:
       up1(field)
       field[x][y] = num_around
    return field


def bf(field, x, y):
    queue = deque([[x, y]])
    while queue:
        row, col = queue.popleft()
        if field[row][col] == False and count_bomb(field, row, col) == 0:
            field[row][col] = 0
        elif field[row][col] == False and count_bomb(field, row, col) > 0:
            field[row][col] = count_bomb(field, row, col)
        

        neighbor_deltas = [(- 1,  0), (- 1, - 1), (- 1, 1),
                           (0, 1), (0, - 1), (1, 0), (1, 1), (1,  - 1)]

        for deltas in neighbor_deltas:
            xd, yd = deltas
            r = row + xd
            c = col + yd 
            if inbounds(field, r, c):
                queue.append([r, c])

def up1(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            field[i][j] = -1
    return field

def count_bomb(field, x, y):
    count = 0

    if field[x][y] == False:
        neighbor_deltas = [(- 1,  0), (- 1, - 1), (- 1, 1),
                           (0, 1), (0, - 1), (1, 0), (1, 1), (1,  - 1)]

        for deltas in neighbor_deltas:
            xd, yd = deltas
            r = x + xd
            c = y + yd 
            if inbounds(field, r, c) and field[r][c] == True:
                count += 1

        return count

def inbounds(field, r, c):
    rowIn = 0 <= r < len(field)
    colIn = 0 <= c < len(field[0])
    
    return rowIn and colIn
    
print(solution(field, x, y))
