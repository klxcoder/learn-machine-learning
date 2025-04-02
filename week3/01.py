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
    p = sigmoid(z)
    print(z, p) # 0.0 0.5

if __name__ == "__main__":
    main()