def solution(n):
    # for i in range(1, n//2):
    #     for p in range(1, n//2):
    #         if i ** p == n:
    #             return True
    for i in range(int(n ** 0.5) + 1):
        for j in range(10):
            if i ** j == n:
                return True
    return False
