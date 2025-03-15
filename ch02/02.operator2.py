# 비교 연산자
#   두 개의 값을 비교하여 그 결과를 불린값(참/거짓, True/Flase)으로 반환하는 연산자이다. 
#   조건문에서 많이 사용되고, 두 값 사이에 관계를 평가하는 코드에서 자주 사용합니다. 

print(1 > 6)                    # False
print(10.7 > 10.6)              # True
print("파이썬" == "파이썬")      # True
print("python" == "Python")     # False
print("python" != "Python")     # True
print(10.7 >= 10.6)

print()


# 논리 연산자
#   하나 이상의 논리적 조건을 조합하여 새로운 논리 결과를 도출하는데 사용된다.
#   조건문에서 많이 사용된다.

print((10 > 5) and (10 > 6)) # True
print((10 > 5) and (10 < 6)) # False
print((10 < 5) and (10 > 6)) # False
print((10 < 5) and (10 < 6)) # False

print()

print((10 > 5) or (10 > 6)) # True
print((10 > 5) or (10 < 6)) # True
print((10 < 5) or (10 > 6)) # True
print((10 < 5) or (10 < 6)) # False

print()

print(not True)  # True -> False
print(not False) # False -> True

print()


# 멤버십 연산자 
#   주어진 값이 시퀀스 자료형인 문자열, 리스트, 튜플 등 특정 대상에 원하는 값이 포함되어 있는지 확인하는 연산자 

print("a" in "apple")           # 포함되어 있다.
print("a" not in "apple")       # 포함되어 있지 않다. 
print("al" in "apple")          # False
print("al" in "ale")            # True
print("a" and "l" in "apple")   # True

