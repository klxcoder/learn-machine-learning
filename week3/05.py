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

    _, axes = plt.subplots(1, 2, figsize=(10, 5))
    # Plot the parabola on the left subplot
    axes[0].scatter([x], [y])
    axes[0].set_title('data')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')

    # Plot the line on the right subplot
    axes[1].plot([0, 1, 2], [0, 1, 2])
    axes[1].set_title('loss')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('y')

    # Adjust layout to prevent overlapping titles
    plt.tight_layout()

    # Display the plot
    plt.show()

    w, b = get_model_parameters()

    for _ in range(10):
        loss = get_loss(x, y, w, b)
        print(loss, w, b)
        """
        0.6931471805599453 0.5 -1
        0.5764321195496719 0.599500008333111 -0.9501249994791696
        0.48673412560681295 0.6866281686153803 -0.9064379909119427
        0.4171689268114933 0.7632290944010446 -0.8680193724968046
        0.362511202835562 0.8309986358938349 -0.8340225872963127
        0.3189361486194237 0.8913912162225908 -0.8037209069861087
        0.28368191715065905 0.9456110145253545 -0.7765122061685206
        0.254755064200958 0.9946390699690512 -0.7519056556714928
        0.2307067735427226 1.0392704510712227 -0.7295032866417702
        0.21047265616051714 1.080150123440894 -0.7089821410783752
        """
        w, b = update(x, y, w, b)

if __name__ == "__main__":
    main()