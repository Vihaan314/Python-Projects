import numpy as np

def getCenterOfRotation(*points):
    points = list(points)
    x1 = np.array(points[0])
    x2 = np.array(points[1])
    y1 = np.array(points[2])
    y2 = np.array(points[3])

    centerPoint1 = (x1 + y1) / 2
    centerPoint2 = (x2 + y2) / 2

    params = np.linalg.inv(np.hstack([(y1 - x1).reshape(-1, 1), (y2 - x2).reshape(-1, 1)]))
    params = np.matmul(params, np.array([[0, 1], [-1, 0]]))
    params = np.matmul(params, np.array(x1 + y1 - x2 - y2).reshape(-1, 1))

    params = params

    t = params[0][0]
    print((y1 - x1) * t)
    print(np.matmul(np.array([[0, 1], [-1, 0]]), (y1 - x1).reshape(-1, 1) * t))
    return (centerPoint1.reshape(-1, 1) * 2 + np.matmul(np.array([[0, 1], [-1, 0]]), (y1 - x1).reshape(-1, 1)) * t) / 2

#print(getCenterOfRotation((1, 4), (1, 2), (3, -4), (3, -2)))

