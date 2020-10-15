from matplotlib.pyplot import savefig
import numpy as np

# Our modules
from utils.integrator import integrator
from utils.other import create_parser, extract_points, plot


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

    # Program defaults
    save_flag = False

    parser = create_parser()
    args = parser.parse_args()

    if args.step:
        step = args.step
    if args.m:
        m = args.m
    if args.k:
        k = args.k
    if args.c:
        c = args.c
    if args.eps:
        eps = args.eps
    if args.max_iters:
        max_iters = args.max_iters
    if args.x_max:
        x_max = args.x_max
    if args.save:
        save_flag = True

    A = np.matrix([
        [      0.,       1.],
        [-(k / m), -(c / m)]
    ], dtype=np.longdouble)

    int_inst = integrator(A, max_iters, eps, step)
    points_info = []

    while True:
        new_point_info = int_inst.next_point(x, y)
        points_info.append(new_point_info)
        x = new_point_info['x']
        y = new_point_info['y']

        if x >= x_max:
            break

    plot(extract_points(points_info), k, c, m, save_flag)


if __name__ == "__main__":
    main()
