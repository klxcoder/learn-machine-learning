import matplotlib.pyplot as plt

def draw_parabola_step_by_step_optimized():
  """Draws a simple parabola step-by-step for integer x values from 0 to 10 with a 300ms delay.
  The grid and axis limits are fixed from the start.
  """
  x_values = []
  y_values = []

  _, ax = plt.subplots()
  ax.set_xlabel("x (Integer)")
  ax.set_ylabel("y = x^2")
  ax.set_title("Simple Parabola (Building Step-by-Step)")
  ax.grid(True)
  ax.set_xticks(range(11)) # Ensure all integer x values are shown
  ax.set_xlim(0, 10)      # Keep the x-axis limits fixed
  ax.set_ylim(0, 100)     # Keep the y-axis limits fixed

  # Set fixed x and y axis limits
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 100)

  # Initialize an empty plot (we'll update its data)
  line, = ax.plot([], [])

  for i in range(11):
    x_values.append(i)
    y_values.append(i**2)

    # Update the data of the existing line object
    line.set_data(x_values, y_values)

    plt.pause(0.3)  # Pause for 300 milliseconds

  plt.show()

if __name__ == '__main__':
  draw_parabola_step_by_step_optimized()