import matplotlib.pyplot as plt

def draw_parabola_step_by_step():
  """Draws a simple parabola step-by-step for integer x values from 0 to 10 with a 300ms delay."""
  x_values = []
  y_values = []

  _, ax = plt.subplots()
  ax.set_xlabel("x (Integer)")
  ax.set_ylabel("y = x^2")
  ax.set_title("Simple Parabola (Building Step-by-Step)")
  ax.grid(True)

  for i in range(11):
    x_values.append(i)
    y_values.append(i**2)

    ax.clear()  # Clear the previous plot
    ax.plot(x_values, y_values)
    ax.set_xlabel("x (Integer)")
    ax.set_ylabel("y = x^2")
    ax.set_title("Simple Parabola (Building Step-by-Step)")
    ax.grid(True)
    ax.set_xticks(range(11)) # Ensure all integer x values are shown

    plt.pause(0.3)  # Pause for 300 milliseconds

  plt.show()

if __name__ == '__main__':
  draw_parabola_step_by_step()