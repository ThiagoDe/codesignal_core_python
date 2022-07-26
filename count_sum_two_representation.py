def solution(n, l, r):  # 2..4
    return sum(1 for a in range(l, r+1) if l <= a <= n - a <= r)
