# 리스트의 다양한 사용법

numbers = [2, 4, 1, 6, 10]
 
# sort() -> 오름차순 정렬 
numbers.sort()
print(numbers)                  # [1, 2, 4, 6, 10]

numbers.sort(reverse=True)      # 내림차순 정렬 
print(numbers)                  # [10, 6, 4, 2, 1]


# 멤버십 연산자 
print(1 in numbers)             # True
print(1 not in numbers)         # False


# index()
#   존재하지 않는 값은 ValueError가 발생한다.
result = numbers.index(10)
print(result)                   # 0 -> 10은 [10, 6, 4, 2, 1]의 "0"번째 자리에 있음. 

