def solution(n):  # 17
    if n == 1:
        return 1
    last = 1
    i = 1
    while i < n:
        if (i * last) >= n:
            return last * i
        last *= i
        i += 1
