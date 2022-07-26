def solution(min1, min2_10, min11, s):
    total = 0
    if s >= min1:
        s -= min1
        total += 1
    if s >= min2_10:  # 17 1
        for m in range(0, 9):
            if s >= min2_10:
                total += 1
                s -= min2_10
    if s >= min11 and total == 10:
        total += s // min11

    return total
