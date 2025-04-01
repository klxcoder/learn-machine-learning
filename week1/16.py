import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
import random
import math

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
    inputs = list(map(lambda x: np.array([abs(x), math.sqrt(abs(x)), x]), xs))
    outputs: list[float] = list(map(lambda input: get_output(weight, input, bias), inputs))
    return (weight, inputs, outputs)

def get_loss(outputs_predicted: list[float], outputs: list[float]) -> float:
    mse: float = sum((yp - yi)**2 for yp, yi in zip(outputs_predicted, outputs)) / len(outputs)
    return mse

def main():

    (weight, inputs, outputs) = get_data()
    weight_predicted: NDArray[np.float64] = np.zeros(len(weight))
    bias_predicted: float = 0
    outputs_predicted: list[float] = list(map(lambda input: get_output(weight_predicted, input, bias_predicted), inputs))

    x_loss = []
    y_loss = []

    def get_weight_derivative() -> NDArray[np.float64]:
        nonlocal outputs_predicted
        small: float = 0.01
        current_loss: float = get_loss(outputs_predicted, outputs)
        derivative: list[float] = []
        for i in range(len(weight_predicted)):
            weight_predicted[i] += small
            outputs_predicted = list(map(lambda input: get_output(weight_predicted, input, bias_predicted), inputs))
            next_loss: float = get_loss(outputs_predicted, outputs)
            derivative.append((next_loss - current_loss) / small)
            weight_predicted[i] -= small
        return np.array(derivative)

    def get_bias_derivative() -> float:
        nonlocal outputs_predicted
        small: float = 0.01
        current_loss: float = get_loss(outputs_predicted, outputs)
        outputs_predicted = list(map(lambda input: get_output(weight_predicted, input, bias_predicted + small), inputs))
        next_loss: float = get_loss(outputs_predicted, outputs)
        return (next_loss - current_loss) / small

    def improve():
        nonlocal weight_predicted
        nonlocal bias_predicted
        alpha: float = 1e-4 # Learning rate
        weight_derivative: NDArray[np.float64] = get_weight_derivative()
        weight_predicted = weight_predicted - alpha * weight_derivative
        bias_derivative: float = get_bias_derivative()
        bias_predicted = bias_predicted - alpha * bias_derivative
        outputs_predicted = list(map(lambda input: get_output(weight_predicted, input, bias_predicted), inputs))
        l: float = get_loss(outputs_predicted, outputs)
        x_loss.append(len(x_loss))
        y_loss.append(l)
        line.set_data(list(map(lambda input: input[-1], inputs)), outputs_predicted)
        loss.set_data(x_loss, y_loss)
        axes[1].relim()
        axes[1].autoscale_view()
        fig.canvas.draw()

    is_mouse_pressed = False

    def on_press(event): # type: ignore
        nonlocal is_mouse_pressed
        is_mouse_pressed = True
        improve()

    def on_motion(event): # type: ignore
        if is_mouse_pressed:
            improve()

    def on_release(event): # type: ignore
        nonlocal is_mouse_pressed
        is_mouse_pressed = False

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    fig.canvas.mpl_connect('button_press_event', on_press)
    fig.canvas.mpl_connect('motion_notify_event', on_motion)
    fig.canvas.mpl_connect('button_release_event', on_release)

    axes[0].set_title('y = f(x)')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')
    axes[0].scatter(list(map(lambda input: input[-1], inputs)), outputs)
    line, = axes[0].plot(list(map(lambda input: input[-1], inputs)), outputs_predicted)
    
    axes[1].set_title('Loss')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('loss')
    loss, = axes[1].plot([], [])

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()