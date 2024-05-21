# Create skew plot from skew()
def plot_skew(genome):
    # y-axis
    skew_vals = skew(genome)
    # x-axis
    positions = range(len(genome) + 1)    
    plt.plot(positions, skew_vals, color='black')
    plt.xlabel('Position (i)')
    plt.ylabel('Skew')
    plt.title('Skew Plot')
    plt.grid(True)
    plt.show()