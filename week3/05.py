import math
import matplotlib.pyplot as plt

def get_data():
    x = 2
    y = 1
    return x, y

def get_model_parameters():
    w = 0.5
    b = -1
    return w, b

def sigmoid(x: float):
    return 1/(1+math.exp(-x))

def get_loss(x: float, y: float, w: float, b: float):
    z = w * x + b
    p = sigmoid(z)
    loss = - (y * math.log(p) + (1 - y) * math.log(1 - p))
    return loss

def update(x: float, y: float, w: float, b: float):
    small = 0.01
    current_loss = get_loss(x, y, w, b)
    dloss_dw = (get_loss(x, y, w + small, b) - current_loss) / small
    dloss_db = (get_loss(x, y, w, b + small) - current_loss) / small
    alpha = 0.1
    w -= alpha * dloss_dw
    b -= alpha * dloss_db
    return w, b

def main():

    x, y = get_data()
    w, b = get_model_parameters()

    _, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the parabola on the left subplot
    axes[0].scatter([x], [y])
    axes[0].plot([x-1, x, x+1], [sigmoid(w*(x-1)+b), sigmoid(w*x+b), sigmoid(w*(x+1)+b)], color='red')
    axes[0].set_title('data')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')

    # Plot the line on the right subplot
    axes[1].set_title('loss')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('y')

    x_loss = []
    y_loss = []

    for _ in range(1000):
        loss = get_loss(x, y, w, b)
        x_loss.append(len(x_loss))
        y_loss.append(loss)
        w, b = update(x, y, w, b)

    axes[1].plot(x_loss, y_loss)

    axes[0].plot([x-1, x, x+1], [sigmoid(w*(x-1)+b), sigmoid(w*x+b), sigmoid(w*(x+1)+b)], color='blue')

        # Adjust layout to prevent overlapping titles
    plt.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()