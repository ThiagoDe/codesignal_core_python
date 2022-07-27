def solution(a0):
    sqr = set([a0])
    arr = list(map(int, str(a0)))
    total = 0
    while total not in sqr:
        for i in range(len(arr)):
            total += (arr[i] ** 2)

        if total in sqr:
            return len(sqr) + 1
        sqr.add(total)
        arr = list(map(int, str(total)))
        total = 0

a0 = 16
# a0 = 103
print(solution(a0))