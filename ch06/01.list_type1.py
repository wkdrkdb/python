a = 20 # 나이
b = 21 # 나이

numbers = [20, 21] # 숫자 요소가 들어있는 리스트 
fruits = ["apple", "banana", "cherry"] # 문자열 요소가 들어있는 리스트 
mixed = [20, "apple", 21, "banana"] # 혼합된 요소가 들어있는 리스트 

print(numbers)
print(fruits)
print(mixed)


# 요소 접근하기
#   리스트명 뒤에 대괄호[]를 입력하고 자료의 위치를 나타내는 인덱스를 사용 
print(fruits[0])
print(fruits[2])


# 슬라이싱 
# 리스트명[시작하는 인덱스:마지막 인덱스 + 1]
print(mixed[0:3])   # [20, 'apple', 21]
print(mixed[1:4])   # ['apple', 21, 'banana']


# IndexError
# print(fruits[3])  -> IndexError: list index out of range


# 마지막 요소에 접근하기 
print(fruits[-1])       # 뒤에서 1번째 -> cherry
print(fruits[-2])       # 뒤에서 2번째 -> banana

# 요소 수정하기 
fruits[0] = "melon"
print(fruits)

# 요소 여러개 수정하기 
mixed[0:2] = [999, 998]
print(mixed)
