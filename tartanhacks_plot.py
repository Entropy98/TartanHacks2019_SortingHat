import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def plot_input_data(something):
    t = np.arange(0.0, 2.0, 0.01)  # x-axis
    #s = 1 + np.sin(2 * np.pi * t)
    s = 1 + np.random.randn(len(t))  # signal wave, need input
    w = np.random.randn(len(t))

    fig_info, ax = plt.subplots()
    ax.plot(t, s, t, w)

    ax.set(xlabel='mm yes', ylabel='brAiN wAaAveS wOoo0oO0',
           title='alpha and delta do some shit')

    ax.grid()
    #fig.savefig("graph.png")
    plt.show()

plot_input_data("yes");
