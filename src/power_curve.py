import numpy as np
import matplotlib.pyplot as plt
from sort import bubble_sort
from load_data import load_data

data = load_data('data/activity.csv')
print(data)

#Power Daten - y-Achse
power_W = data['PowerOriginal']

sorted_power_W = bubble_sort(power_W)
sorted_power_W = sorted_power_W[::-1]

# Time Daten - x-Achse
time_seg_sec = len(data['PowerOriginal']) / 1805 # Zeit pro Aufzeichnung in Sekunden
print(time_seg_sec)

time_x = np.arange(len(sorted_power_W)) * time_seg_sec  # Zeit pro Punkt
time_x = time_x / 60  # Zeit in Minuten
print(time_x)

# Plotting
plt.plot(time_x, sorted_power_W, color="green")
plt.xlabel('Zeit in min')
plt.ylabel('Power in W')
plt.title('Sakai 1 - Power Curve')
plt.grid()
plt.savefig('figures/power_curve.png')