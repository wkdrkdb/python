import matplotlib.pyplot as plt

figure = plt.figure()
axes1 = figure.add_subplot(1, 1, 1)
# axes2 = figure.add_subplot(1, 2, 2)

# 꺽은 선 그래프 구현하기 
x = [0, 1, 2, 3, 4] # X축
y = [4, 1, 3, 5, 2] # Y축

# 추가 
x2 = [0, 1, 2, 3, 4]
y2 = [3, 2, 5, 7, 1]

axes1.plot(x, y, linestyle = "dotted", linewidth = "3.0", color = 'green', marker = 'o')
axes1.plot(x2, y2, linestyle = "dashed", color = 'red')

plt.title('Example Graph')
plt.xlabel('Count')
plt.ylabel('Grade')

plt.show()
