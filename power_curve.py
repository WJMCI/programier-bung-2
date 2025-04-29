from load_data import load_data
from sort import bubble_sort
import numpy as np
import matplotlib.pyplot as plt

data = load_data('activity.csv')
power_W = data['PowerOriginal']
sorted_power_W = bubble_sort(power_W)
def time_array():
    time=np.arange(0, len(power_W), 1)
    return time/60
print(time_array())


def plot_power_curve(sorted_power_W, time_array):
    plt.figure(figsize=(10, 5))
    plt.plot(time_array(), sorted_power_W, label='Power Curve', color='blue')
    plt.title('Power Curve')
    plt.xlabel('Time (min)')
    plt.ylabel('Power (W)')
    plt.grid()
    plt.legend()
    plt.show()
    plt.savefig('power_curve.png')

plot_power_curve(sorted_power_W[::-1], time_array)
