MAX_SIZE = 1000000


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def onSegment(p, q, r):
    return max(p.x, r.x) >= q.x >= min(p.x, r.x) and max(p.y, r.y) >= q.y >= min(p.y, r.y)


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    if val == 0:
        return 0

    if val > 0:
        return 1
    return 2


def doIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and onSegment(p1, p2, q1):
        return True

    if o2 == 0 and onSegment(p1, q2, q1):
        return True

    if o3 == 0 and onSegment(p2, p1, q2):
        return True

    if o4 == 0 and onSegment(p2, q1, q2):
        return True

    return False


def isInside(polygon, p):
    n = len(polygon)

    if n < 3:
        return False

    extreme = Point(MAX_SIZE, p.y)

    count = 0
    i = 0

    while True:
        next = (i + 1) % n

        if doIntersect(polygon[i], polygon[next], p, extreme):
            if orientation(polygon[i], p, polygon[next]) == 0:
                return onSegment(polygon[i], p, polygon[next])
            count += 1
        i = next
        if i == 0:
            break
    return (count % 2) == 1