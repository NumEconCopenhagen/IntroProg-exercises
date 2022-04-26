fig = plt.figure(dpi = 100, figsize=(7,4))
ax = fig.add_subplot(1,1,1)
levels = np.sort([j*10**(-i) for i in [-1,0,1,2,3,4] for j in [0.5,1,1.5]])
cs = ax.contour(x1_grid,x2_grid,f_grid,levels=levels,cmap=cm.jet)
fig.colorbar(cs);