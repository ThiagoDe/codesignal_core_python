def solution(param1, param2):
    res = ''
    list1 = list(map(int, list(str(param1))))
    list2 = list(map(int, list(str(param2))))
    while list1 and list2:
        n1 = list1.pop()
        n2 = list2.pop()
        res = str((n1 + n2) % 10) + res

    if list1:
        res = ''.join(map(str, list1)) + res
    if list2:
        res = ''.join(map(str, (list2))) + res

    return int(res)
