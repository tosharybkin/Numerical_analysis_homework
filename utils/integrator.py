from math import sqrt
import numpy as np
from matplotlib import pyplot as plt
from numpy import matrixlib


class integrator:

    def __init__(self, matrix: np.matrix,
                 max_iters: float,
                 eps: float,
                 step: float) -> None:

        self._matrix = matrix
        self._eps = eps
        self._max_iters = max_iters
        self._step = step
        self._mul_count = 0
        self._div_count = 0
        self.max_error = 0


    def _system(self, y_vec: np.array) -> np.matrix:
        return y_vec.dot(self._matrix)


    def _RK3(self, x: float, y_vec: np.array, step: float) -> dict:
        k1 = self._system(y_vec)
        k2 = self._system(y_vec + (k1 * step / 3))
        k3 = self._system(y_vec + (k2 * step * 2 / 3))

        x_next = x + step
        y_vec_next = y_vec + step * ((1 / 4) * k1 + (3 / 4) * k3)

        return {'x': x_next, 'y': y_vec_next}


    def next_point(self, x, y_vec) -> dict:
        iter_counter = 0

        while True:
            iter_counter += 1

            old_step = self._step

            whole_step  = self._RK3(x, y_vec, self._step)
            half_step_1 = self._RK3(x, y_vec, self._step / 2.)
            half_step_2 = self._RK3(half_step_1['x'],
                                   half_step_1['y'],
                                   self._step / 2.)

            delta = whole_step['y'] - half_step_2['y']
            error = np.linalg.norm(delta)

            if error > self._eps and iter_counter <= self._max_iters + 1:
                self._step /= 2.
                self._div_count += 1

            else:
                x = whole_step['x']
                y_vec = whole_step['y']

                if error < self._eps / (2 ** (3 + 1)):
                    self._step *= 2.
                    self._mul_count += 1

                if error > self.max_error:
                    self.max_error = error

                break

        return {'x': x, 'y': y_vec, 'y2': half_step_2['y'],
                'error': error, 'step': old_step,
                'mul_count': self._mul_count,
                'div_count': self._div_count
                }
