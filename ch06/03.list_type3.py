list_a = [1, 2, 3]
list_b = [4, 5, 6]

# +연산자
list_c = list_a + list_b
print(list_c)               # [1, 2, 3, 4, 5, 6]

# *연산자
list_d = list_a * 3
print(list_d)               # [1, 2, 3, 1, 2, 3, 1, 2, 3]

list_e = [*list_a]
print(list_e)               # [1, 2, 3]


###################################################################################################


# 리스트 요소 추가하기
string_list = ["안", "녕", "하", "세", "요"]

# append() - 마지막에 데이터 하나 추가 
string_list.append("?")
print(string_list)          # ['안', '녕', '하', '세', '요', '?']

# insert() - 측정 위치에 데이터 하나 추가 
string_list.insert(2, "!")
print(string_list)          # ['안', '녕', '!', '하', '세', '요', '?']

# extend() - 여러 개의 데이터를 추가
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print(list_a + list_b)      # [1, 2, 3, 4, 5, 6]
print(list_a)               # [1, 2, 3]                -> 비파괴적

list_a.extend(list_b)
print(list_a)               # [1, 2, 3, 4, 5, 6]       -> 파괴적 


# 리스트 요소 삭제하기 
#   인덱스로 제거 / 값으로 제거 

# 인덱스로 제거 (del) 
del list_b[1]
print(list_b)               # [4, 6]

list_b = [4, 5, 6]
del list_b[1:3]             # del list_b[1:] 와 같음 , del list_b[:1]하면 6만 남고, del list_b[:]를 하면 모두 지워짐
print(list_b)               # [4]

# 인덱스로 제거 (pop())
list_b = [4, 5, 6]
result = list_b.pop(1)               
print(list_b)               # [4, 6]
print(result)               # 5 -> pop()을 사용하면 어떤 값이 지워졌는지 알 수 있음 


# 값으로 제거 (remove())
list_b = [4, 5, 4, 6]
list_b.remove(4)        
print(list_b)               # [5, 4, 6] -> 중복된 값이 있는 경우 맨 앞의 인덱스만 제거한다.


# 전체 제거 (clear())
list_b = [4, 5, 6]
list_b.clear()
print(list_b)               # []








