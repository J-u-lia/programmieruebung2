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

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(time, sorted_power_W, color='blue', linewidth=2)

ymin = -20
ymax = 450
ax.set_ylim(ymin, ymax)
ax.set_yticks([0, 100, 200, 300, 400])
ax.set_yticklabels([f"{y} W/kg" for y in [0, 100, 200, 300, 400]])

xmin = -1
xmax = 31
ax.set_xlim(xmin, xmax)
ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
ax.set_xticklabels([f"{x} min" for x in [0, 5, 10, 15, 20, 25, 30]])


#ax.set_ylim(bottom=-1)
#ax.set_xlim(left=-0.5, right=31)
#yticks = ax.get_yticks()
#ax.set_yticks(yticks)
#ax.set_yticklabels([f"{int(y)} W/kg" for y in yticks])
#xticks = ax.get_xticks()
#ax.set_xticks(xticks)
#ax.set_xticklabels([f"{int(x)} min" for x in xticks])

plt.xlabel("Zeit [min]")
plt.ylabel("Leistung [W/kg]")
plt.grid()
plt.title("Leistungskurve I")
plt.tight_layout()


plt.savefig('C:/Users/famro/git/programmieruebung2/figures/Leistungskurve_I.png')
plt.show()