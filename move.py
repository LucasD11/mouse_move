import time
import math
from pymouse import PyMouse


def main():
    mouse = PyMouse()
    x_dim, y_dim = mouse.screen_size()
    r = x_dim / 10
    while True:
        for part in range(100):
            degree = part / 100 * math.pi * 2
            x = x_dim / 2 + r * math.sin(degree)
            y = x_dim / 2 + r * math.cos(degree)
            mouse.move(x, y)
            time.sleep(0.1)


if __name__ == "__main__":
    main()
