import numpy as np
import matplotlib.pyplot as plt
from load_data import load_data
from sort import bubble_sort


data = load_data('activity.csv')
power_W = data['PowerOriginal']
print(power_W)
sorted_power_W = bubble_sort(power_W)
print(sorted_power_W[::-1])

time = np.arange(1804, 0, -1)
time = time / 60 

fig,ax = plt.subplots(figsize=(10, 5))

ax.plot(time, sorted_power_W, color='blue')
plt.xlabel("Zeit [min]")

ymin = -20
ymax = 450
ax.set_ylim(ymin, ymax)
ax.set_yticks([0, 100, 200, 300, 400])
ax.set_yticklabels([f"{y} W/kg" for y in [0, 100, 200, 300, 400]])


#ymin = 0
#ymax = max(sorted_power_W) + 1
#ax.set_ylim(ymin, ymax)
#ax.set_yticks(np.linspace(ymin, ymax, 6))
#ax.set_yticklabels([f"{int(y)} W/kg" for y in np.linspace(ymin, ymax, 6)])

plt.ylabel("Leistung [W/kg]")
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.title("Leistungstest")

plt.savefig('C:/Users/famro/git/programmieruebung2/figures/Leistungskurve I.png')
plt.show()