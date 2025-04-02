import math

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

def update(x: float, y: float, w: float, b: float):
    z = w * x + b
    p = sigmoid(z)
    dloss_dp = (1-y)/(1-p) - y/p
    dp_dz = p * (1 - p)
    dloss_dz = dloss_dp * dp_dz
    dloss_dw = dloss_dz * x
    dloss_db = dloss_dz
    alpha = 0.1
    w -= alpha * dloss_dw
    b -= alpha * dloss_db
    return w, b

def get_loss(x: float, y: float, w: float, b: float):
    z = w * x + b
    p = sigmoid(z)
    loss = - (y * math.log(p) + (1 - y) * math.log(1 - p))
    return loss

def main():
    x, y = get_data()
    w, b = get_model_parameters()
    loss = get_loss(x, y, w, b)
    print(loss) # 0.6931471805599453
    w, b = update(x, y, w, b)
    print(w) # 0.6
    print(b) # -0.95
    loss = get_loss(x, y, w, b)
    print(loss) # 0.5759394198788437 < 0.6931471805599453

if __name__ == "__main__":
    main()