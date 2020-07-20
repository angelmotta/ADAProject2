def getWeightUtil(match):
    if isinstance(match[0], int) and isinstance(match[1], int):
        return match[0] / match[1]
    # Division
    elif isinstance(match[0], int):
        wBlock = match[0]
        sumBlocksB = 0
        for i in match[1]:
            sumBlocksB += i
        return wBlock / sumBlocksB
    # Agrupacion
    else:
        wBlock = match[1]
        sumBlocksA = 0
        for i in match[0]:
            sumBlocksA += i
        return sumBlocksA / wBlock


def getWeight(match):
    if len(match) == 0: return 0
    w = 0
    for i in match:
        w += getWeightUtil(i)
    return w


def getMinWeigthMatch(matchesList):
    if len(matchesList) == 0: return None
    minWeight = matchesList[0]
    for match in matchesList:
        if getWeight(match) < getWeight(minWeight):
            minWeight = match
    return minWeight
