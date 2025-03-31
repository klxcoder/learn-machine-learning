import matplotlib.pyplot as plt

def draw_simple_parabola():
  """Draws a simple parabola for integer x values from 0 to 10."""
  x = list(range(11))  # Integer x values from 0 to 10
  y = [val**2 for val in x]  # Simple parabola equation: y = x^2

  plt.plot(x, y)
  plt.xlabel("x (Integer)")
  plt.ylabel("y = x^2")
  plt.title("Simple Parabola (x from 0 to 10)")
  plt.grid(True)  # Add a grid for better readability
  plt.xticks(x)  # Ensure all integer x values are shown on the x-axis
  plt.show()

if __name__ == '__main__':
  draw_simple_parabola()