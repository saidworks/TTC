from matplotlib.pyplot import show,plot,axis,legend

# default data for axes
# pyplot.axes()
# pyplot.show()

# given values
x, y, z= [i for i in range(6)],[j**2 for j in range(6)], [j**3 for j in range(6)]
plot(x,y,label="squares",marker='*',color='red',markeredgecolor='blue')
plot(x,z,label="cubes",marker='o',color='green',markeredgecolor='green')
axis([0,5,0,25])
legend()
show()

