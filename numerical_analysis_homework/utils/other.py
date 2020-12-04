import numpy as np


class Points:
    def __init__(self, xs, v_1s, v_2s):
        self.xs = xs
        self.v_1s = v_1s
        self.v_2s = v_2s


def extract_points(points_info: dict) -> dict:
    xs = np.array([0], dtype=np.longdouble)
    v_1s = np.array([10], dtype=np.longdouble)
    v_2s = np.array([0], dtype=np.longdouble)

    for point in points_info:
        xs = np.append(xs, point['x'])
        v_1s = np.append(v_1s, point['y'].item((0, 0)))
        v_2s = np.append(v_2s, point['y'].item((0, 1)))

    return Points(xs, v_1s, v_2s)
