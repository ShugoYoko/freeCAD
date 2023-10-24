import matplotlib.pyplot as plt
import matplotlib.patches as pat

fig, axs = plt.subplots(1, 1, figsize=(10, 5))

#三角形
vertices=[(0.2, 0.2), (0.8, 0.2), (0.7, 0.6)]
p = pat.Polygon(xy=vertices,fc="w", ec="k")
#頂点表示
display=["A","B","C"]
for j, vertex in enumerate(vertices):
   axs.text(vertex[0], vertex[1], display[j], ha='left', va='top')
#角度
wa = pat.Wedge((0.2,0.2) ,0.070, theta1=0, theta2 = 39, fc="w",ec="k")
wb = pat.Wedge((0.8,0.2) ,0.070, theta1=105, theta2 = 180, fc="w",ec="k")
wc = pat.Wedge((0.7,0.6) ,0.070, theta1=219, theta2 = 284, fc="w",ec="k")
    
axs.add_patch(p)
axs.add_patch(wa)
axs.add_patch(wb)
axs.add_patch(wc)

axs.set_xlim(0.1, 0.9)
axs.set_ylim(0.1, 0.9)
axs.axis('off')
axs.set_aspect('equal')

plt.show()