#Uses python3
import sys
import math

def get_points_distance(point1, point2):
    return (math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2)))

def minimum_distance(points, is_sorted):
    min_dist = math.inf
    if len(points) <= 1:
        pass
    elif len(points) == 2:
        min_dist = get_points_distance(points[0], points[1])
    else:
        if is_sorted == False:
            points.sort(key=lambda x: x[0])
        
        x_mid = len(points) // 2
        left_points = points[:x_mid]
        right_points = points[x_mid:]
        min_dist_left = minimum_distance(left_points, is_sorted=True)
        min_dist_right = minimum_distance(right_points, is_sorted=True)
        min_dist = min(min_dist_left, min_dist_right)
        
        x_center = (left_points[-1][0] + right_points[0][0]) / 2
        center_points = [point for point in points if (x_center - min_dist) <= point[0] <= (x_center + min_dist)]
        center_points.sort(key=lambda y: y[1])
        for p in range(len(center_points)):
            pivot_point = center_points[p]
            q = p + 1
            while q < len(center_points) and (center_points[q][1] <= pivot_point[1] + min_dist):
                dist = get_points_distance(pivot_point, center_points[q])
                if dist < min_dist:
                    min_dist = dist
                q += 1

    return (min_dist)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = zip(*[x, y])
    points = [list(row) for row in points]
    print("{0:.9f}".format(minimum_distance(points, is_sorted=False)))
