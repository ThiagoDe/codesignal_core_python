def solution(arr):
    if len(arr) % 2 != 0:
        return arr
    else:
        mid = len(arr) // 2
        n = arr[mid] + arr[(mid - 1)]
        return arr[:mid - 1] + [n] + arr[mid + 1:]

