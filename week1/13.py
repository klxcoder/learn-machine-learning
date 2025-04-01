import matplotlib.pyplot as plt
import random

_, axes = plt.subplots(1, 2, figsize=(10, 5))
line, = axes[0].plot([], [])

def f(x: float, model: tuple[float, float, float, float]):
    (a, b, c, d) = model
    return a*x**3 + b*x**2 + c*x + d

def get_data():
    a = random.choice(range(5))
    b = random.choice(range(5))
    c = random.choice(range(5))
    d = random.choice(range(5))
    model: tuple[float, float, float, float] = (a, b, c, d)
    x = list(range(-10, 11))
    y = [f(_, model) + 2 * random.random() for _ in x]
    return (model, x, y)

(model, x, y) = get_data()

x_loss = []
y_loss = []

model_predicted: tuple[float, float, float, float] = (0., 0., 0., 0.)

is_mouse_pressed = False

def get_derivative() -> tuple[float, float, float, float]:
    small: float = 0.01
    current_lost: float = get_lost(model_predicted)

    derivative = (
        (get_lost((model_predicted[0] + small, model_predicted[1], model_predicted[2], model_predicted[3])) - current_lost) / small,
        (get_lost((model_predicted[0], model_predicted[1] + small, model_predicted[2], model_predicted[3])) - current_lost) / small,
        (get_lost((model_predicted[0], model_predicted[1], model_predicted[2] + small, model_predicted[3])) - current_lost) / small,
        (get_lost((model_predicted[0], model_predicted[1], model_predicted[2], model_predicted[3] + small)) - current_lost) / small,
    )

    return derivative

def get_lost(model: tuple[float, float, float, float]) -> float:
    y_predicted: list[float] = [f(_, model) for _ in x]
    mse: float = sum((yp - yi)**2 for yp, yi in zip(y_predicted, y)) / len(y)
    return mse

alpha = 0.000001

def improve():
    global model_predicted

    derivative: tuple[float, ...] = get_derivative()
    model_predicted = (
        model_predicted[0] - alpha * derivative[0],
        model_predicted[1] - alpha * derivative[1],
        model_predicted[2] - alpha * derivative[2],
        model_predicted[3] - alpha * derivative[3],
    )

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
    (a, b, c, d) = model
    axes[0].scatter(x, y)
    axes[0].set_title(f'y = {a}*x**3 + {b}*x**2 + {c}*x + {d} + noise')
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