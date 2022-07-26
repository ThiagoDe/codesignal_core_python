n = 1445
n = 15
def solution(n):  # 1445
    res = ''
    nums = list(map(int,(list(str(n)))))
    print(nums)
    i = len(nums) - 1
    rem = False
    while i >= 0:
        if i == 0:
            # print(nums[i], '0')
            res = str(nums[i]) + res
        else:
            if rem:
                nums[i] += 1
            if nums[i] >= 5:
                rem = True
            else:
                rem = False
            res = '0' + res
        i -= 1

    if rem:
        print(res[0])
        zero = int(res[0]) + 1
        res = str(zero) + res[1:]

    # print(res)
    return int(res) 

print(solution(n))