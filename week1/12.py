import matplotlib.pyplot as plt
import random

_, axes = plt.subplots(1, 2, figsize=(10, 5))
line, = axes[0].plot([], [])

def f(x: float, model: list[float]):
    (a, b, c) = model
    return a * x * x + b * x + c

def get_data():
    a = random.choice(range(5))
    b = random.choice(range(5))
    c = random.choice(range(5))
    model: list[float] = [a, b, c]
    x = list(range(-10, 11))
    y = [f(_, model) + 2 * random.random() for _ in x]
    return (model, x, y)

(model, x, y) = get_data()

x_loss = []
y_loss = []

model_predicted: list[float] = [0., 0., 0.]

is_mouse_pressed = False

def get_derivative() -> tuple[float, ...]:
    small: float = 0.01
    current_lost: float = get_lost(model_predicted)

    derivative: list[float] = []

    for i in range(len(model_predicted)):
        _model_predicted: list[float] = list(model_predicted)
        _model_predicted[i] += small
        next_loss: float = get_lost(_model_predicted)
        derivative.append((next_loss - current_lost) / small)

    return tuple(derivative)

def get_lost(model: list[float]) -> float:
    y_predicted: list[float] = [f(_, model) for _ in x]
    mse: float = sum((yp - yi)**2 for yp, yi in zip(y_predicted, y)) / len(y)
    return mse

alpha = 0.0001

def improve():
    global model_predicted
    derivative: tuple[float, ...] = get_derivative()
    for i in range(len(model_predicted)):
        model_predicted[i] -= alpha * derivative[i]

    # Plot the predicted line
    line.set_data(x, [f(_, model_predicted) for _ in x])
    
    # Plot the loss
    x_loss.append(len(x_loss))
    y_loss.append(get_lost(model_predicted))
    axes[1].plot(x_loss, y_loss)

    fig = plt.gcf()
    fig.canvas.draw() # Force a redraw of the figure

def on_press(event): # type: ignore
    global is_mouse_pressed
    if event.inaxes == axes[0] or event.inaxes == axes[1]: # Only trigger if click is within the axes
        is_mouse_pressed = True
        improve() # Call improve immediately on press

def on_motion(event): # type: ignore
    global is_mouse_pressed
    if is_mouse_pressed and (event.inaxes == axes[0] or event.inaxes == axes[1]):
        improve()

def on_release(event): # type: ignore
    global is_mouse_pressed
    is_mouse_pressed = False

def gradient_descent():
    (a, b, c) = model
    axes[0].scatter(x, y)
    axes[0].set_title(f'y = {a} * x * x + {b} * x + {c} + noise')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')

    axes[1].set_title('Loss')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('loss')

    fig = plt.gcf()

    fig.canvas.mpl_connect('button_press_event', on_press)
    fig.canvas.mpl_connect('motion_notify_event', on_motion)
    fig.canvas.mpl_connect('button_release_event', on_release)

    # Adjust layout to prevent overlapping titles
    plt.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    gradient_descent()