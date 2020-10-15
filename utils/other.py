import argparse
import numpy as np
import matplotlib.pyplot as plt

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Integrator tool',
    )

    parser.add_argument(
        '--step', type=float, required=False
    )

    parser.add_argument(
        '--k', type=float, required=False
    )

    parser.add_argument(
        '--c', type=float, required=False
    )

    parser.add_argument(
        '--eps', type=float, required=False
    )
    parser.add_argument(
        '--max_iters', type=int, required=False
    )

    parser.add_argument(
        '--x_max', type=float, required=False
    )

    parser.add_argument(
        '--m', type=float, required=False
    )

    parser.add_argument(
        '--save', action='store_true'
    )

    parser.add_argument(
        '--print', action='store_true'
    )

    return parser

def extract_points(points_info: dict) -> dict:
    xs = np.array([0], dtype=np.longdouble)
    us = np.array([10], dtype=np.longdouble)
    ys = np.array([0], dtype=np.longdouble)

    for point in points_info:
        xs = np.append(xs, point['x'])
        us = np.append(us, point['y'].item((0, 0)))
        ys = np.append(ys, point['y'].item((0, 1)))

    return {'xs': xs, 'us': us, 'ys': ys}


def plot(points: dict, k: float, c: float,
         m: float, save_flag: bool) -> None:
    fig, axs = plt.subplots(2, 1, figsize=(8, 8))
    plt.subplots_adjust(hspace=0.3)
    title = f"Task 11:_K_=_{k},_C_=_{c},_M_=_{m}"
    fig.canvas.set_window_title(title)

    axs[0].plot(points['xs'], points['ys'], label = "y(x)")
    axs[0].plot(points['xs'], points['us'], label = "u(x)")
    axs[0].legend()
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("u(x)/y(x)")

    axs[1].plot(points['ys'], points['us'], label = "u(y)")
    axs[1].legend()
    axs[1].set_xlabel("y")
    axs[1].set_ylabel("u(y)")

    if save_flag:
        plt.savefig(r"img/" + f"K-{k:.1f}_C-{c:.1f}" + ".png")
    else:
        plt.show()
