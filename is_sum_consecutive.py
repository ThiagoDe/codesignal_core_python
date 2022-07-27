n = 9

def solution(n):
    r = [x for x in range(1, n)]
    i = 0
    j = 1
    count = 0
    while j < len(r):
        if sum(r[i:j+1]) == n:
            count += 1
            i += 1
            j = i + 1
        elif sum(r[i:j+1]) > n:
            i += 1
            j = i + 1
        else:
            j += 1

    print(r)
    return count
    
print(solution(n))