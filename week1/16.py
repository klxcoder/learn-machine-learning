"""
inputs: vector[]
input: vector = [x**3, x**2, x]
x: float
output: vector = [y]
outputs: vectors
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
import random

def get_output(weight: NDArray[np.float64], input: NDArray[np.float64], bias: float) -> float:
    return np.dot(weight, input) + bias

def get_data():
    weight: NDArray[np.float64] = np.array([
        random.choice(range(-5, 6)),
        random.choice(range(-5, 6)),
        random.choice(range(-5, 6)),
    ])
    bias: float = random.choice(range(-5, 6))
    xs: list[int] = list(range(-20, 21))
    inputs = list(map(lambda x: np.array([x**3, x**2, x]), xs))
    outputs = list(map(lambda input: get_output(weight, input, bias), inputs))
    return (weight, bias, inputs, outputs)

def main():

    def on_press(event): # type: ignore
        print('pressed')

    (weight, bias, inputs, outputs) = get_data()
    weight_predicted: NDArray[np.float64] = np.array([0, 0, 0])
    bias_predicted: float = 0
    outputs_predicted = list(map(lambda input: get_output(weight_predicted, input, bias_predicted), inputs))

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    fig.canvas.mpl_connect('button_press_event', on_press)

    axes[0].set_title('y = f(x)')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')
    axes[0].scatter(list(map(lambda input: input[-1], inputs)), outputs)
    axes[0].plot(list(map(lambda input: input[-1], inputs)), outputs_predicted)
    
    axes[1].set_title('Loss')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('loss')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()