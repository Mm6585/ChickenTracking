import math

def measure_dist(x1, y1, x2, y2, box1, box2):
    coor_dist = math.sqrt(math.pow((x1-x2), 2) + math.pow((y1 - y2), 2))
    box_dist = max(box1, box2) / min(box1, box2)
    box_dist = 1

    if (coor_dist == 0):
        distance = box_dist
    elif (box_dist == 0):
        distance = coor_dist
    else:
        distance = coor_dist * box_dist

    return distance
