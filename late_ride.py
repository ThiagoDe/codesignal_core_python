def solution(n):
    h = n // 60
    m = n % 60
    sp = sum(map(int, ''.join(list(map(str, [h, m])))))
    return sp
