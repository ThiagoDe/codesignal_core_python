arr = [7, 2, 2, 5, 10, 7]

def solution(arr):
    if len(arr) % 2 == 0:

        mid = len(arr) // 2 # avoid float number 
        print(mid)
        print(arr[mid])
        n = arr[mid] + arr[(mid - 1)] # index int
        return arr[0] == n and arr[-1] == n
    else:
        mid = len(arr) // 2
        return arr[0] == arr[mid] and arr[-1] == arr[mid]


print(solution(arr))