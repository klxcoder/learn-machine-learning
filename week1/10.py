import matplotlib.pyplot as plt
import random

_, axes = plt.subplots(1, 2, figsize=(10, 5))
line, = axes[0].plot([], [])

def f(x: float, m: float, b: float):
    return m * x + b

def get_data():
    m = random.choice(range(5))
    b = random.choice(range(5))
    x = list(range(0, 11))
    y = [f(_, m, b) + 2 * random.random() for _ in x]
    return (m, b, x, y)

(m, b, x, y) = get_data()

x_loss = []
y_loss = []

m_predicted: float = 0
b_predicted: float = 0

is_mouse_pressed = False

def get_derivative():
    small = 0.001
    derivative_b = (get_lost(m_predicted, b_predicted + small) - get_lost(m_predicted, b_predicted))/small
    derivative_w = (get_lost(m_predicted + small, b_predicted) - get_lost(m_predicted, b_predicted))/small
    return (derivative_b, derivative_w)

def get_lost(m: float, b: float):
    y_predicted = [f(_, m, b) for _ in x]
    mse = sum((yp - yi)**2 for yp, yi in zip(y_predicted, y)) / len(y)
    return mse

alpha = 0.01

def improve():
    global m_predicted, b_predicted

    (derivative_b, derivative_w) = get_derivative()

    m_predicted -= alpha * derivative_w
    b_predicted -= alpha * derivative_b

    # Plot the predicted line
    line.set_data(x, [f(_, m_predicted, b_predicted) for _ in x])
    
    # Plot the loss
    x_loss.append(len(x_loss))
    y_loss.append(get_lost(m_predicted, b_predicted))
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
    
    axes[0].scatter(x, y)
    axes[0].set_title(f'y = {m} * x + {b} + noise')
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