# def solution(m, n):

    # def ycoord(x):
    #     return -(n/m) * x + n

    # tot = 0

    # for x in range(m):
    #     start = ycoord(x)
    #     if start % 1 == 0 and x > 0:
    #         tot += 1
    #     end = ycoord(x+1)
    #     if end % 1 == 0 and x < m-1:
    #         tot += 1
    #     start = math.ceil(start)
    #     end = math.floor(end)
    #     covered = math.ceil(start - end)

    #     tot += covered
    # return tot
