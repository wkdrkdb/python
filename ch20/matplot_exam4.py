import matplotlib.pyplot as plt 

figure = plt.figure()

axes = figure.add_subplot(1, 1, 1)

data = [1, 2, 3]
label = ["Good", "Bad", "Normal"]
axes.pie(data, labels=label, autopct="%d%%")

plt.axis('equal')
plt.legend(label, loc="center left")

plt.show()