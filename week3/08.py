import matplotlib.pyplot as plt

def get_data():
    xs = [[1, 1], [2, 2]]
    ys = [0, 1]
    return xs, ys

def main():
    xs, ys = get_data()

    _, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the data on the left subplot
    fail_label_added = False
    pass_label_added = False

    for i in range(len(xs)):
        if ys[i] == 0:
            axes[0].scatter(xs[i][0], xs[i][1], marker='o', color='red', label='Fail' if not fail_label_added else "")
            fail_label_added = True
        else:
            axes[0].scatter(xs[i][0], xs[i][1], marker='s', color='blue', label='Pass' if not pass_label_added else "")
            pass_label_added = True

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