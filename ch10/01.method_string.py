"""
객체(object)
    물리적, 추상적 개념을 프로그램으로 표현한 것 
    예) 물리적 - 자동차, 컴퓨터, 리모컨
        추상적 - 주문, 배송
        
메소드(method)
    특정 객체가 가지고 있는 함수를 의미한다.
    객체.메소드()
"""


# String 객체 format 메소드 
print("10자리 폭 왼쪽 정렬 '{:<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 '{:>10d}'".format(123))
print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))
print()
print("10자리 폭 왼쪽 정렬 채움문자 '{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움문자 '{:*>10d}'".format(123))
print("10자리 폭 가운데 정렬 채움문자 '{:*^10d}'".format(123))


gender = 1
print("주민등록번호: 060522-{:*<7d}".format(gender))


# count() 메소드 
s = "내가 그린 기린 그림은 목이 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다."
result = s.count("기린")
print(result)

s = "best of best"
result = s.count("best", 5)     # 5번째 인덱스(o)부터 best가 몇 번 나왔는지  
print(result)                   # 1


# find() 메소드 - 위치한 인덱스 번호 반환
"""
  str:   a p p l e
index:   0 1 2 3 4
"""

s = "apple"
reuslt = s.find("p")            # p라는 문자가 apple의 몇 번째 인덱스에 있는지 
print(result)

result = s.rfind("p")           # 뒤에서부터 찾음 
print(result)

# index() - find() 메소드와 같지만 문자열이 존재하지 않을 경우 에러!
s = "apple"
result = s.index("p")
print(result)

"""
result = s.index("z")
print(result)               # 에러 발생

result = s.find("z")
print(result)               # -1 
"""
