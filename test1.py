import pandas as pdb
import numpy as np
import scipy.io as spio
import matplotlib.pyplot as plt
from matplotlib import cm
import sys
import mysql.connector

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.set_axis_bgcolor('grey')
ax1.axis("Off")
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax1.title.set_text('First Plot')
ax2.title.set_text('Second Plot')
ax3.title.set_text('Third Plot')
ax4.title.set_text('Fourth Plot')
plt.show()



x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# Four axes, returned as a 2-d array
f, axarr = plt.subplots(2, 2)
axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('Axis [0,0]')
axarr[0, 0].set_yticklabels([])
axarr[0, 0].set_xticklabels([])

axarr[0, 0].set_axis_bgcolor('white')

axarr[0, 1].scatter(x, y)
axarr[0, 1].set_title('Axis [0,1]')
axarr[0, 0].set_axis_bgcolor('grey')
#axarr[0, 1].axis("Off")
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title('Axis [1,0]')
#axarr[1, 0].axis("Off")
axarr[1, 1].scatter(x, y ** 2)
axarr[1, 1].set_title('Axis [1,1]')
#axarr[1, 1].axis("Off")
# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
#plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
#plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

plt.show()