a_list = [1, 2, 3]
b_list = [[1,2,3], [4, 5, 6]]

print(b_list[0])        # [1, 2, 3]
print(b_list[0][1])     # 2 

c_list = [[[1, 2, 3], 7, 8], [[4, 5, 6], 9, 10]]

print(c_list[0][0][1])  # 2 

# c_list의 값이 4인 요소에 접근하여 출력하세요.
print(c_list[1][0][0])

# c_list의 값이 7인 요소에 접근하여 출력하세요. 
print(c_list[0][1])


d_list = ["apple"]
print(d_list[0])        # apple
print(d_list[0][0])     # a 0
