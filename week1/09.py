import matplotlib.pyplot as plt
import random

_, axes = plt.subplots(1, 2, figsize=(10, 5))
line, = axes[0].plot([], [])

def get_data():
    m = random.choice(range(5))
    b = random.choice(range(5))
    x = list(range(0, 11))
    y = [m * _ + b + 2 * random.random() for _ in x]
    return (m, b, x, y)

(m, b, x, y) = get_data()

x_loss = []
y_loss = []

def on_click_figure(_):
    improve()

def improve():
    # Plot the predicted line
    m_predicted = random.random()
    b_predicted = random.random()
    line.set_data(x, [m_predicted * _ + b_predicted for _ in x])
    
    # Plot the loss
    x_loss.append(len(x_loss))
    y_loss.append(random.random())
    axes[1].plot(x_loss, y_loss)

    fig = plt.gcf()
    fig.canvas.draw() # Force a redraw of the figure

def gradient_descent():
    
    axes[0].scatter(x, y)
    axes[0].set_title(f'y = {m} * x + {b} + noise')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')

    axes[1].set_title('Loss')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('loss')

    fig = plt.gcf()
    fig.canvas.mpl_connect('button_press_event', on_click_figure)

    # Adjust layout to prevent overlapping titles
    plt.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    gradient_descent()