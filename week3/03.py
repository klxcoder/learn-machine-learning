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

    for _ in range(10):
        loss = get_loss(x, y, w, b)
        print(loss, w, b)
        """
        0.6931471805599453 0.5 -1
        0.5759394198788437 0.6 -0.95
        0.4859279106088488 0.6875646998228404 -0.9062176500885798
        0.41617735327557165 0.7645394698658768 -0.8677302650670615
        0.36142022986315236 0.8326268129855113 -0.8336865935072443
        0.3178012009528347 0.893289579263519 -0.8033552103682404
        0.2825377675475174 0.9477400893566357 -0.7761299553216822
        0.2536229933768928 0.9969664554226877 -0.7515167722886562
        0.22959940147951688 1.0417695957974171 -0.7291152021012914
        0.20939709443915755 1.0827992047473105 -0.7086003976263447
        """
        w, b = update(x, y, w, b)

if __name__ == "__main__":
    main()