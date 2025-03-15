"""
mutable(가변) - 메모리에 저장된 값을 변경 가능 
    ex. 리스트(list), 세트(set), 릭셔너리(dict) ...등 

immutable(불가변) - 메모리에 저장된 값 변경 불가
    ex. 정수(int), 실수(float), 문자열(str), 튜플(tuple) ...등
"""


# mutable 예 
me = [1, 2, 3]
print(me)           # [1, 2, 3]
print(id(me))       # 2444895169024

me.append(4)
print(me)           # [1, 2, 3, 4]
print(id(me))       # 2444895169024



# immutable 예 
me2 = 10
print(me2)
print(id(me2))      # 140718390053592

me2 += 1
print(me2)
print(id(me2))      # 140718390053624


