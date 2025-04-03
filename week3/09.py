import numpy as np

xs = [[2, 60], [3, 70], [6, 85], [8, 90], [4, 75], [7, 80]]

# Convert the list of lists to a NumPy array
np_xs = np.array(xs)

# Extract the first column (index 0)
xs0 = np_xs[:, 0].tolist()

# Extract the second column (index 1)
xs1 = np_xs[:, 1].tolist()

print(f"xs0 = {xs0}")
print(f"xs1 = {xs1}")