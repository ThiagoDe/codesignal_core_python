def solution(l, r):
    hash = {}
    res = 0
    pairs = {}
    for n in range(l, r + 1):  # 11
        digSum = sum(list(map(int, str(n))))
        left = list(range(n - digSum, n))
        right = list(range(n + 1, n + digSum + 1))
        conf = left + right

        hash[n] = conf

    for k in range(l, r + 1):
        for m in hash[k]:
            if m in hash and k in hash[m]:
                res += 1

    return res // 2


def getKey(n, hash):
    keys = []
    for k, v in hash.items():
        if n in v:
            keys.append(k)
    return keys

l = 10
r = 12

print(solution(l, r))