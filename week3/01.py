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

def main():
    x, y = get_data()
    w, b = get_model_parameters()
    z = w * x + b
    # print(z) # 0.0
    p = sigmoid(z)
    # print(p) # 0.5
    loss = - (y * math.log(p) + (1 - y) * math.log(1 - p))
    # print(loss) # 0.6931471805599453
    dloss_dp = (1-y)/(1-p) - y/p
    # print(dloss_dp) # -2.0
    dp_dz = p * (1 - p)
    # print(dp_dz) # 0.25
    dloss_dz = dloss_dp * dp_dz
    # print(dloss_dz) # -0.5

if __name__ == "__main__":
    main()