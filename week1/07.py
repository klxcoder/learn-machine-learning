import matplotlib.pyplot as plt

def axes_example():
    # Generate x values from 0 to 10 (using a step for smoother curves)
    x = list(range(0, 11)) # Integer values
    # To get smoother curves, you can use a step like 0.1
    # x = [i * 0.1 for i in range(0, 101)]

    # Calculate y values for the parabola
    y_parabola = [val**2 for val in x]

    # Calculate y values for the line
    y_line = x

    # Create a figure and two subplots side by side
    _, axes = plt.subplots(2, 1, figsize=(5, 10))

    # Plot the parabola on the left subplot
    axes[0].plot(x, y_parabola)
    axes[0].set_title('Parabola: y = x*x')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')

    # Plot the line on the right subplot
    axes[1].plot(x, y_line)
    axes[1].set_title('Line: y = x')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('y')

    # Adjust layout to prevent overlapping titles
    plt.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    axes_example()