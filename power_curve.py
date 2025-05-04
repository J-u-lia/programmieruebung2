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

fig, ax = plt.subplots()

ax.plot(time, sorted_power_W, color='blue', linewidth=2)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0, right=30)
yticks = ax.get_yticks()
ax.set_yticks(yticks)
ax.set_yticklabels([f"{int(y)} W/kg" for y in yticks])
xticks = ax.get_xticks()
ax.set_xticks(xticks)
ax.set_xticklabels([f"{int(x)} min" for x in xticks])
plt.xlabel("time [min]")
plt.ylabel("Leistung [W/kg]")
plt.grid()
plt.title("Leistungskurve I")

plt.savefig('C:/Users/famro/git/programmieruebung2/figures/Leistungskurve I.png')
plt.show()