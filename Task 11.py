from math import sqrt
import numpy as np
import pylab


#  <----HOW NOT TO FORGET THE SYSTEM OF ODE---->
#  u' = x               |      u = y1   |
#                       |  ->           |  ->
#  x' = -(cx + ku) / m  |      x = y2   |
#
#      y1 = 0*y1 +    1*y2
#  ->
#      y2 = 2*y1 - 0.15*y2
#
#* Method: Runge-Kutta 3th order

K = 3
C = 0.15


#  Returns (y', u')
def func(x, y, u) -> np.array:
    return np.array([-C * y - K * u, y])


def RK3(x, y, u, step) -> np.array:
    k1_y, k1_u = func(x, y, u)
    k2_y, k2_u = func(x + step / 3, y + (step / 3) * k1_y,
                      u + (step / 3) * k1_u)
    k3_y, k3_u = func(x + (2 * step / 3),
                      y + (2 * step / 3) * k2_y,
                      u + (2 * step / 3) * k2_u)

    x_next = x + step
    y_next = y + step * ((1 / 4) * k1_y + (3 / 4) * k3_y)
    u_next = u + step * ((1 / 4) * k1_u + (3 / 4) * k3_u)

    return np.array([x_next, y_next, u_next])


def main() -> None:

    global K, C

    #? Initial conditions:
    x0 = 0
    y0 = 0
    u0 = 10
    xmax = 50
    max_iters = 10000

    #! User defined constants
    step = 1
    eps = 0.0001
    K = 3
    C = 0.15

    x, y, u = x0, y0, u0
    xs = np.array([])
    ys = np.array([])
    us = np.array([])

    iter_counter = 0

    while True:
        while True:
            iter_counter += 1

            whole_step = RK3(x, y, u, step)
            half_step1 = RK3(x, y, u, step / 2)
            half_step2 = RK3(*half_step1, step / 2)

            error = sqrt((whole_step[1] - half_step2[1]) ** 2
                         + (whole_step[2] - half_step2[2]) ** 2)

            if error > eps and iter_counter <= max_iters + 1:
                step /= 2.
            elif error < eps / (2 ** (3 + 1)):
                step *= 2.
                break
            else:
                x, y, u = whole_step
                break

        xs = np.append(xs, [x])
        ys = np.append(ys, [y])
        us = np.append(us, [u])

        if x > xmax:
            break


    pylab.figure(1)
    pylab.plot(xs, us, label = "u(x)")
    pylab.plot(xs, ys, label = "y(x)")
    pylab.legend()

    pylab.figure(2)
    pylab.plot(ys, us, label = "u(y)")
    pylab.legend()

    pylab.show()

if __name__ == "__main__":
    main()
