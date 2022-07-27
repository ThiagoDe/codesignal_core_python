statues = [6, 2, 3, 8]

def solution(statues):
    sor = set(sorted(statues))
    total = 0
    for n in range(min(sor), max(sor) + 1):
        if n not in sor:
            total += 1
        
    return total 

print(solution(statues))