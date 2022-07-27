def solution(current, numberOfDigits):  # 21 5d
    lastPage = current  # 1
    prev = lastPage
    # nextPage = lastPage + 1 #22
    while (numberOfDigits + 1): # 5
        digNeed = len(str(lastPage))
        if numberOfDigits >= digNeed:
            numberOfDigits -= digNeed
            prev = lastPage
            lastPage = lastPage + 1
        else:
            return prev

current = 1
numberOfDigits = 5
print(solution(current, numberOfDigits))