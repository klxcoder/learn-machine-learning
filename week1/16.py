"""
inputs: vector[]
input: vector = [x**3, x**2, x]
x: float
output: vector = [y]
outputs: vectors
"""

import numpy as np
from numpy.typing import NDArray

def get_output(weight: NDArray[np.float64], input: NDArray[np.float64], bias: float) -> float:
    return np.dot(weight, input) + bias
