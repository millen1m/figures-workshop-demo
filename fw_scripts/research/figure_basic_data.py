import numpy as np
import matplotlib.pyplot as plt


def create(y_extra):
    x = np.linspace(0, 5, 100)
    y = np.sin(x) + x + y_extra

    fig, subplots = plt.subplots(nrows=2)
    subplots[0].plot(x, y)
    fig.savefig('hello.png')
    plt.show()


if __name__ == '__main__':
    y_e = 5
    create(y_extra=y_e)

