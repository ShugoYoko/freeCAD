import matplotlib.pyplot as plt
import matplotlib.patches as pat
import math

fig, axs = plt.subplots(1, 1, figsize=(10, 5))
xmin = -1
xmax = 1
ymin = -1
ymax = 1

plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
plt.plot([0,math.cos(math.radians(30))],[0,math.sin(math.radians(30))], 'g')
plt.plot([0,math.cos(math.radians(150))],[0,math.sin(math.radians(150))], 'g')
p=pat.Circle(xy=(0, 0), radius=1, fc='w', ec='r')
axs.text(math.cos(math.radians(30)),math.sin(math.radians(30)),"(x,y)")
axs.text(math.cos(math.radians(150)),math.sin(math.radians(150)),"(-x,y)")

axs.set_xlim(-1, 1)
axs.set_ylim(-1, 1)
axs.axis('off')
axs.add_patch(p)
axs.set_aspect('equal')


plt.show()