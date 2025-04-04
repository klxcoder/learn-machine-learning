import matplotlib.pyplot as plt
import math

def get_data():
    xs: list[list[float]] = [[2, 60], [3, 70], [6, 85], [8, 90], [4, 75], [7, 80]]
    ys = [0, 0, 1, 1, 0, 1]
    xs_scaled: list[list[float]] = list(map(lambda x: [x[0], x[1]/100], xs))
    return xs, ys, xs_scaled

def get_model_parameters():
    b0, b1, b2 = 1, 1, 1
    return b0, b1, b2

def sigmoid(x: float):
    return 1/(1+math.exp(-x))

def get_p(x: list[float], y: float, b0: float, b1: float, b2: float):
    z = b0 + b1 * x[0] + b2 * x[1]
    p = sigmoid(z)
    return p

def get_loss(x: list[float], y: float, b0: float, b1: float, b2: float):
    p = get_p(x, y, b0, b1, b2)
    loss = - (y * math.log(p) + (1 - y) * math.log(1 - p))
    return loss

def get_derivative(x: list[float], y: float, b0: float, b1: float, b2: float, current_loss: float):
    small = 0.01
    dloss_db0 = (get_loss(x, y, b0 + small, b1, b2) - current_loss) / small
    dloss_db1 = (get_loss(x, y, b0, b1 + small, b2) - current_loss) / small
    dloss_db2 = (get_loss(x, y, b0, b1, b2 + small) - current_loss) / small
    return dloss_db0, dloss_db1, dloss_db2

def main():
    xs, ys, xs_scaled = get_data()
    b0, b1, b2 = get_model_parameters()

    _, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the data on the left subplot
    fail_label_added = False
    pass_label_added = False

    for i in range(len(xs)):
        if ys[i] == 0:
            axes[0].scatter(xs[i][0], xs[i][1], marker='o', color='red', label='Fail' if not fail_label_added else "")
            fail_label_added = True
        else:
            axes[0].scatter(xs[i][0], xs[i][1], marker='s', color='blue', label='Pass' if not pass_label_added else "")
            pass_label_added = True

    x1s = list(map(lambda x: x[0], xs))
    x2s = list(map(lambda x1: (-b0 - b1 * x1) / b2, x1s))
    x2s_scaled: list[float] = list(map(lambda x: x * 100, x2s))
    axes[0].plot(x1s, x2s_scaled, color='red')

    axes[0].set_title('data')
    axes[0].set_xlabel('x1 (Hours Studied)')
    axes[0].set_ylabel('x2 (Previous Grade)')

    # Plot the loss on the right subplot
    axes[1].set_title('loss')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('loss')

    x_loss: list[float] = []
    y_loss: list[float] = []

    alpha = 0.1 # learning rate
    
    loss = get_loss(xs_scaled[0], ys[0], b0, b1, b2)
    x_loss.append(len(x_loss))
    y_loss.append(loss)

    for _ in range(1000):
        sum_loss = 0
        sum_dloss_db0 = 0
        sum_dloss_db1 = 0
        sum_dloss_db2 = 0
        for x, y in zip(xs_scaled, ys):
            loss = get_loss(x, y, b0, b1, b2)
            sum_loss += loss
            dloss_db0, dloss_db1, dloss_db2 = get_derivative(x, y, b0, b1, b2, loss)
            sum_dloss_db0 += dloss_db0
            sum_dloss_db1 += dloss_db1
            sum_dloss_db2 += dloss_db2
        b0 -= alpha * sum_dloss_db0 / len(xs)
        b1 -= alpha * sum_dloss_db1 / len(xs)
        b2 -= alpha * sum_dloss_db2 / len(xs)

        x_loss.append(len(x_loss))
        y_loss.append(sum_loss/len(xs))

    axes[1].plot(x_loss, y_loss)

    x1s = list(map(lambda x: x[0], xs))
    x2s = list(map(lambda x1: (-b0 - b1 * x1) / b2, x1s))
    x2s_scaled: list[float] = list(map(lambda x: x * 100, x2s))
    axes[0].plot(x1s, x2s_scaled, color='blue')

    # Adjust layout to prevent overlapping titles
    plt.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()