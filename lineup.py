def solution(commands):
    count = 0
    same = True
    for com in commands:
        if com == 'L' or com == 'R':
            same = not same
            if same == True:
                count += 1
        if com == "A" and same == True:
            count += 1

    return count
