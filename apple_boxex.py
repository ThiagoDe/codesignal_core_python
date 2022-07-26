k = 5
def solution(k):
    y = 0
    r = 0

    for i in range(1, k + 1):
        if i % 2 != 0:
            y += (i * i)
        else:
            r += (i * i)

    return r - y


print(solution(k))