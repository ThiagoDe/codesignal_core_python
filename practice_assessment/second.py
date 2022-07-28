# You are given a string s. Your task is to count the number of ways of splitting s into three non-empty parts a, b and c (s=a + b + c) in such a way that a + b, b + c and c + a are all different strings.
# NOTE: + refers to string concatenation.
# Example
# For s = "xzxzx", the output should be solution(s) = 5.
# Consider all the ways to split s into three non-empty parts:
# * If a = "x", b = "z" and c = "xzx", then all a + b = "xz", b + c = "zxzx" and c + a = xzxx are different.
# * If a = "x", b = "zx" and c = "zx", then all a + b = "xzx", b + c = "zxzx" and c + a = zxx are different.
# * If a = "x", b = "zxz" and c = "x", then all a + b = "xzxz", b + c = "zxzx" and c + a = xx are different.
# * If a = "xz", b = "x" and c = "zx", then a + b = b + c = "xzx". Hence, this split is not counted.
# * If a = "xz", b = "xz" and c = "x", then all a + b = "xzxz", b + c = "xzx" and c + a = xxz are different.
# * If a = "xzx", b = "z" and c = "x", then all a + b = "xzxz", b + c = "zx" and c + a = xxzx are different.
# Since there are five valid ways to split s, the answer is 5.
s = "xzxzx"
def solution(s):
    res = 0
    i = 1
    j = 2
    
    while i <= len(s) - 2:
        while j <= len(s) - 1:
            
            a = s[:i]
            b = s[i:j]
            c = s[j:]
            print(a,b,c)
            j += 1
            # if a + b != b + c and a + c ! put it in an list an check for same
            arr = [a + b, b + c, c + a]
            # print(arr)
            # print(set(arr))
            if len(arr) == len(set(arr)):
                res += 1
        i += 1
        j = i + 1

    return res 

print(solution(s))
