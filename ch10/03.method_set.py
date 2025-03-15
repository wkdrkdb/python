#  교집합 intersectio() 메소드

s1 = {"apple", "banana", "cherry"}
s2 = {"apple", "banana", "orange"}

result = s1.intersection(s2)       
print(result)                   # {'banana', 'apple'} -> s1, s2의 교집합

print(s1 & s2)                  # s1, s2 교집합


# 합집합 union() 메소드
s1 = {"apple", "banana", "cherry"}
s2 = {"apple", "banana", "orange"}
result = s1.union(s2)
print(result)                   # {'banana', 'cherry', 'orange', 'apple'}

print(s1 | s2)                  # s1, s2 합집합


# 차집합 difference() 메소드
s1 = {"apple", "banana", "cherry"}
s2 = {"apple", "banana", "orange"}
result = s1.difference(s2)
print(result)                   # {'cherry'} 

print(s1 - s2)                  # s1, s2 차집합




