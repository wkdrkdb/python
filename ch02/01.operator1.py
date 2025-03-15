# 산술 연산자

x = 5
y = 2

print(x + y)
print(x - y)
print(x * y)    # 곱하기 연산 
print(x / y)    # 나누기 연산


print(x // y)   # 몫 구하기
print(x % y)    # 나머지 구하기 
print(x ** y)   # 제곱 


# 문자열을 사용한 연산자 
tag1 = "#나는솔로"
tag2 = "#솔로탈출?"
tag3 = "#저는 최종선택을 하지 않겠습니다"

tag = tag1 + tag2 + tag3
print(tag)                  #  #나는솔로#솔로탈출?#저는 최종선택을 하지 않겠습니다


message = "아자!\n" * 5
print(message)



# 복합할당연산자
#   복합할당연산자는 변수에 새로운 값을 계산하고, 그 결과를 다시 그 변수에 할당하는 연산자이다.
#   기존 변수의 값을 가져와서 연산한  후에 다시 해당 변수에 저장한다.

x = 5

# x에 3을 더하고, 다시 x변수에 저장 
x += 3       # x = x + 3
print(x)

# x에 2를 빼고, 다시 x변수에 저장
x -= 2       # x = x - 2
print(x)

x *= 4       # x = x * 4
print(x)

x /= 2       # x = x / 2
print(x)
