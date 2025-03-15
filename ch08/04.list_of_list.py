list_of_list = [[1, 2, 3], [4, 5, 6]]

for list in list_of_list:
    print(list)
    for number in list:
        print(number)




output = ""

for i in range(1, 10):
    for j in range(0, i):
        output += "*"   # 별 누적
    output += "\n"      # 줄바꿈 처리            

print(output)