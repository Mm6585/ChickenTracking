import math

def measure_dist(x1, y1, x2, y2):
    distance = math.sqrt(math.pow((x1-x2), 2) + math.pow((y1 - y2), 2))
    return distance
