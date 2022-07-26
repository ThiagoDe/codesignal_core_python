def solution(score1, score2):
    if score1 > 7 or score2 > 7:
        return False
    if 7 in [score1, score2] and min([score1, score2]) in [5, 6]:
        return True
    if 6 in [score1, score2] and min([score1, score2]) < 5:
        return True

    return False
