"""
함수는 작업을 수행한 결과를 반환(return)할 수 있다.
반환된 값은 함수 호출한 위치에서 사용할 수 있다.
"""

# 반환 값이 있는 함수(매개변수 x, 리턴값 o)
def address():
    str = "우편번호 12345\n"
    str += "서울시 영등포구 여의도동"
    return str      # 생성된 문자열 반환

# 함수 호출 후 반환된 값을 result 변수에 저장

result = address()
print(result)


# 매개변수 o, 리턴값 o 
def plus(num1, num2):       # num1 = 5, num2 = 7
    return num1 + num2      # 두 매개변수의 합을 반환


result = plus(5, 7)
print(result)


print(plus(2,3))


print(plus(plus(3, 5), plus(1, 9)))

