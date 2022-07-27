def solution(n, a):
    if n <= 1:
        return a
    b = [0] * n
    for i in range(n):
        if i == 0:
            b[i] = a[0] + a[1]
        elif i == (n - 1):
            b[i] = a[n - 1] + a[n - 2]
        else:
            b[i] = a[i - 1] + a[i] + a[i + 1]

    return b
