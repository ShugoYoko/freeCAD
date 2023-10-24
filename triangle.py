import matplotlib.pyplot as plt
import matplotlib.patches as pat

fig, axs = plt.subplots(1, 3, figsize=(10, 5))

for i in range(3):
    #三角形
    vertices=[(0.2, 0.2), (0.8, 0.2), (0.8, 0.8)]
    p = pat.Polygon(xy=vertices,fc="w", ec="k")
    #頂点表示
    display=["A","B","C"]
    for j, vertex in enumerate(vertices):
       axs[i].text(vertex[0], vertex[1], display[j], ha='left', va='top')
    #角度
    w = pat.Wedge((0.2,0.2) ,0.075, theta1=0, theta2 = 45, fc="w",ec="k")
    #直角
    right_angle=[(0.75,0.2),(0.8,0.2),(0.8,0.25),(0.75,0.25)]
    right=pat.Polygon(xy=right_angle,fc="w", ec="k")

    axs[i].add_patch(p)
    axs[i].add_patch(w)
    axs[i].add_patch(right)

    axs[i].set_xlim(0.1, 0.9)
    axs[i].set_ylim(0.1, 0.9)
    axs[i].axis('off')
    axs[i].set_aspect('equal')

plt.show()