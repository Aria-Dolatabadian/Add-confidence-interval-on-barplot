import numpy as np
import matplotlib.pyplot as plt
# width of the bars
barWidth = 0.3
# Choose the height of the blue bars
bars1 = [10, 9, 10]
# Choose the height of the cyan bars
bars2 = [8, 10, 8]
# Choose the height of the error bars (bars1)
yer1 = [0.5, 0.9, 0.5]
# Choose the height of the error bars (bars2)
yer2 = [1, 0.7, 1]
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
# Create blue bars
plt.bar(r1, bars1, width=barWidth, color='blue', edgecolor='black', yerr=yer1, capsize=7, label='Wheat')
# Create cyan bars
plt.bar(r2, bars2, width=barWidth, color='cyan', edgecolor='black', yerr=yer2, capsize=7, label='Barley')
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C'])
plt.ylabel('Height')
plt.legend()
plt.show()
