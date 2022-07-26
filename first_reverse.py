arr = [1, 2, 3, 4, 5]
# arr = []

def solution(arr):
    if len(arr) <= 1: return arr
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr

print(solution(arr))
