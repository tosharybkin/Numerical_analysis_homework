import numpy as np
import matplotlib.pyplot as plt

STEP = 0.01
EPS = 0.01

#  Returns (y', u')
def func(x, y, u):
    return np.array((-0.15 * y - 2 * u, y))

def RK3(x, y, u, step):
    k1_y, k1_u = func(x, y, u)
    k2_y, k2_u = func(x + step / 3, y + (step / 3) * k1_y, 
                      u + (step / 3) * k1_u)
    k3_y, k3_u = func(x + (2 * step / 3), 
                       y + (2 * step / 3) * k2_y, u + (step/3) * k2_u)

    x_next = x + step
    y_next = y + step * ((1 / 4) * k1_y + (3 / 4) * k3_y)
    u_next = u + step * ((1 / 4) * k1_u + (3 / 4) * k3_u)
    
    return np.array(x_next, y_next, u_next)

def step_control(x, y, u, step):
    whole_step = RK3(x, y, u, step)
    half_step1 = RK3(x, y, u, step/2)
    half_step2 = RK3(*half_step1, step/2)
    
def main():
    pass

if __name__ == "__main__":
    main()
