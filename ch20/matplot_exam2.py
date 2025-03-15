import matplotlib.pyplot as plt

figure = plt.figure()

axes = figure.add_subplot(111) # 1, 1, 1 과 동일 

x = ["Mon", "Tue", "Wed", "Tur", "Fri", "Sat", "Sun"]
y = [1, 11, 3, 8, 14, 5, 7]

# 바 그래프 만들기 
axes.bar(x, y)

plt.title("Bar Graph")
plt.xlabel("Week")
plt.ylabel("Value")

plt.savefig('./data/example.png', dpi = 300, format='png')
plt.show()
