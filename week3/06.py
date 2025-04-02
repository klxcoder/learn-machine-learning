import math
import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt

def get_data():
    xs: NDArray[np.float64] = np.array(list(range(20)))
    ys: list[int] = list(map(lambda x: 0 if x < 10 else 1, xs))
    return xs, ys

def get_model_parameters():
    w = 0
    b = 0
    return w, b

def sigmoid(x: float):
    return 1/(1+math.exp(-x))

def get_loss(x: float, y: float, w: float, b: float):
    z = w * x + b
    p = sigmoid(z)
    loss = - (y * math.log(p) + (1 - y) * math.log(1 - p))
    return loss

def get_derivative(x: float, y: float, w: float, b: float, current_loss: float):
    small = 0.01
    dloss_dw = (get_loss(x, y, w + small, b) - current_loss) / small
    dloss_db = (get_loss(x, y, w, b + small) - current_loss) / small
    return dloss_dw, dloss_db

def main():

    xs, ys = get_data()
    w, b = get_model_parameters()

    _, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the parabola on the left subplot
    axes[0].scatter(xs, ys)
    axes[0].plot(xs, list(map(lambda x: sigmoid(w*x+b), xs)), color='red')
    axes[0].set_title('data')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')

    # Plot the line on the right subplot
    axes[1].set_title('loss')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('y')

    x_loss = []
    y_loss = []

    alpha = 0.1 # learning rate

    for _ in range(1000):
        sum_loss = 0
        sum_dloss_dw = 0
        sum_dloss_db = 0
        for x, y in zip(xs, ys):
            loss = get_loss(x, y, w, b)
            sum_loss += loss
            dloss_dw, dloss_db = get_derivative(x, y, w, b, loss)
            sum_dloss_dw += dloss_dw
            sum_dloss_db += dloss_db
        x_loss.append(len(x_loss))
        y_loss.append(sum_loss/len(xs))
        w -= alpha * sum_dloss_dw / len(xs)
        b -= alpha * sum_dloss_db / len(xs)

    axes[1].plot(x_loss, y_loss)

    axes[0].plot(xs, list(map(lambda x: sigmoid(w*x+b), xs)), color='blue')

    # Adjust layout to prevent overlapping titles
    plt.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()