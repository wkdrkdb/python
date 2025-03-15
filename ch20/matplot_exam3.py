import matplotlib.pyplot as plt

figure = plt.figure() 

axes = figure.add_subplot(1, 1, 1)

x = [1, 2, 3, 4, 5, 6]
y = [5, 1, 3, 2, 5, 10]
areas = [50, 100, 150, 200, 250, 300]
colors = ['red', 'green', 'blue', 'orange', 'aqua', 'crimson']

axes.scatter(x, y, s=areas, c=colors)

plt.show()