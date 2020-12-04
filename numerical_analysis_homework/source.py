import numpy as np

# Our modules
from numerical_analysis_homework.utils.integrator import Integrator
from numerical_analysis_homework.utils.other import extract_points


def main() -> None:

    # Default values for parameters
    # Problem parameters
    m = 1
    k = 2
    c = 0.15

    # Method parameters
    step = 0.01
    eps = 0.0001
    max_iters = 10000
    x_max = 10

    # Initial conditions
    x = 0
    y = np.array([10, 0], dtype=np.longdouble)

    A = np.matrix([
        [      0.,       1.],
        [-(k / m), -(c / m)]
    ], dtype=np.longdouble)

    integrator = Integrator(A, eps, step)
    points_info = []

    while True:
        new_point_info = integrator.next_point(x, y)
        points_info.append(new_point_info)
        x = new_point_info['x']
        y = new_point_info['y']

        if x >= x_max:
            break

    print(f"Max local error: {integrator.max_error}")



if __name__ == "__main__":
    main()
