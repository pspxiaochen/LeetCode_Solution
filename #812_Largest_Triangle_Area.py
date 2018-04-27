def largestTriangleArea(points):
    maxArea = 0.0
    for i in range(len(points)):
        for j in range(len(points)):
            for k in range(len(points)):
                a = 0.5 * abs(points[i][0] * points[j][1] + points[j][0] * points[k][1] + points[k][0] * points[i][1] - points[i][0] * points[k][1] - points[j][0] * points[i][1]
                           - points[k][0] * points[j][1])
                if a > maxArea:
                    maxArea = a
    return maxArea

