import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

from numpy.matrixlib.defmatrix import matrix


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


# # Return 1 x 2 matrix (y_vec must be shaped to 1 x 2)
# def system(matrix: np.matrix, y_vec: np.array) -> np.matrix:
#     return y_vec.dot(matrix)

#  Returns (y', u')
def func(x, y, u) -> np.array:
    return np.array([-0.15 * y - 2 * u, y])

# def RK3(matrix: np.matrix, x: float, y_vec: np.array, step: float):
#     k1 = system(matrix, y_vec)
#     k2 = system(matrix, y_vec + (k1 * step / 3))
#     k3 = system(matrix, y_vec + (k2 * step * 2 / 3))
    
#     x_next = x + step
#     y_vec_next = y_vec + step * ((1 / 4) * k1 + (3 / 4) * k3)
    
#     return x_next, y_vec_next
    

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

# def error(x, y, u, step) -> float:
#     whole_step = RK3(x, y, u, step)
#     half_step1 = RK3(x, y, u, step / 2)
#     half_step2 = RK3(*half_step1, step / 2)
    
#     return sqrt((whole_step[1] - half_step2[1]) ^ 2
#                  + (whole_step[2] - half_step2[2]) ^ 2)
    
def main() -> None:
    
    #? Initial conditions:
    x0 = 0
    y0 = 2
    u0 = 1
    
    xmax = 10
    
    #! User defined constants
    step = 0.01
    eps = 0.01
    
    x, y, u = x0, y0, u0
    xs = np.array([])
    ys = np.array([])
    us = np.array([])
    
    iter_counter = 0
    
    while True:
        while True:
            whole_step = RK3(x, y, u, step)
            half_step1 = RK3(x, y, u, step / 2)
            half_step2 = RK3(*half_step1, step / 2)
            
            error = sqrt((whole_step[1] - half_step2[1]) ** 2
                         + (whole_step[2] - half_step2[2]) ** 2)
            
            if error > eps:
                step /= 2.
            elif error < eps / (2 ^ (3 + 1)):
                step *= 2.
                break
            else:
                x, y, u = whole_step
                break

        xs = np.append(xs, [x])
        ys = np.append(ys, [y])
        us = np.append(us, [u])
        
        iter_counter += 1
        
        if x > xmax:
            break
    
    plt.plot(xs, ys)
    plt.show()
        

if __name__ == "__main__":
    main()
