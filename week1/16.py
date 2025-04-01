"""
inputs: vector[]
input: vector = [x**3, x**2, x]
x: float
output: vector = [y]
outputs: vectors
"""

import numpy as np
from numpy.typing import NDArray
import random

def get_output(weight: NDArray[np.float64], input: NDArray[np.float64], bias: float) -> float:
    return np.dot(weight, input) + bias

def get_data():
    weight: NDArray[np.float64] = np.array([
        random.choice(range(-5, 6)),
        random.choice(range(-5, 6)),
        random.choice(range(-5, 6)),
    ])
    bias: float = 0
    xs: list[int] = list(range(-20, 21))
    input = list(map(lambda x: x, xs))
    return (weight, bias, input)