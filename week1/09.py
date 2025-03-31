import matplotlib.pyplot as plt
import random

def get_data():
    m = random.choice(range(5))
    b = random.choice(range(5))
    x = list(range(0, 11))
    y = [m * _ + b + 2 * random.random() for _ in x]
    return (m, b, x, y)

def on_click_figure(_):
    print('Clicked')

def improve(x: list[int], x_loss: list[int], y_loss: list[int], line, axes): # type: ignore
    # Plot the predicted line
    m_predicted = random.random()
    b_predicted = random.random()
    line.set_data(x, [m_predicted * _ + b_predicted for _ in x])
    
    # Plot the loss
    x_loss.append(0)
    y_loss.append(0)
    axes[1].plot(x_loss, y_loss)

def gradient_descent():
    (m, b, x, y) = get_data()

    _, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].scatter(x, y)
    axes[0].set_title(f'y = {m} * x + {b} + noise')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')

    line, = axes[0].plot([], [])

    axes[1].set_title('Loss')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('loss')

    x_loss = []
    y_loss = []

    for _ in range(10):
        improve(x, x_loss, y_loss, line, axes)
        plt.pause(0.5)

    fig = plt.gcf()
    fig.canvas.mpl_connect('button_press_event', on_click_figure)

    # Adjust layout to prevent overlapping titles
    plt.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    gradient_descent()