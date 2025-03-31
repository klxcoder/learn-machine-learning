import matplotlib.pyplot as plt

def axes_example():
    # Generate x values from 0 to 10 (using a step for smoother curves)
    x = list(range(0, 11)) # Integer values
    # To get smoother curves, you can use a step like 0.1
    # x = [i * 0.1 for i in range(0, 101)]

    # Create a figure and two subplots side by side
    _, axes = plt.subplots(2, 2, figsize=(10, 10))

    # Plot the subplot on the top left
    axes[0, 0].plot(x, [0 * val + 0 for val in x])
    axes[0, 0].set_title('Parabola top left: y = 0x + 0')
    axes[0, 0].set_xlabel('x')
    axes[0, 0].set_ylabel('y')
    axes[0, 0].set_xlim(0, 10)
    axes[0, 0].set_ylim(0, 11)

    # Plot the subplot on the top right
    axes[0, 1].plot(x, [0 * val + 1 for val in x])
    axes[0, 1].set_title('Parabola top right: y = 0x + 1')
    axes[0, 1].set_xlabel('x')
    axes[0, 1].set_ylabel('y')
    axes[0, 1].set_xlim(0, 10)
    axes[0, 1].set_ylim(0, 11)

    # Plot the subplot on the bottom left
    axes[1, 0].plot(x, [1 * val + 0 for val in x])
    axes[1, 0].set_title('Parabola bottom left: y = 1x + 0')
    axes[1, 0].set_xlabel('x')
    axes[1, 0].set_ylabel('y')
    axes[1, 0].set_xlim(0, 10)
    axes[1, 0].set_ylim(0, 11)

    # Plot the subplot on the bottom right
    axes[1, 1].plot(x, [1 * val + 1 for val in x])
    axes[1, 1].set_title('Parabola bottom right: y = 1x + 1')
    axes[1, 1].set_xlabel('x')
    axes[1, 1].set_ylabel('y')
    axes[1, 1].set_xlim(0, 10)
    axes[1, 1].set_ylim(0, 11)

    # Adjust layout to prevent overlapping titles
    plt.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    axes_example()