import matplotlib.pyplot as plt

def main():
    _, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the data on the left subplot
    axes[0].set_title('data')
    axes[0].set_xlabel('x1 (hours of study)')
    axes[0].set_ylabel('x2 (hours of sleep)')

    # Plot the loss on the right subplot
    axes[1].set_title('loss')
    axes[1].set_xlabel('t')
    axes[1].set_ylabel('loss')

    # Adjust layout to prevent overlapping titles
    plt.tight_layout()

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()