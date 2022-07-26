def solution(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if elemToReplace == inputArray[i]:
            inputArray[i] = substitutionElem

    return inputArray
