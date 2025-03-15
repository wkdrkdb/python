# 삼항 연산자 
#   삼항 연산자는 프로그래밍에서 사용되는 조건부 연산자입니다.
#   3개의 피연산자를 가지고 조건에 따라 값을 반환하는 연산자입니다. 

"""
참일 때 값 if (조건) else 거짓일 때 값
"""

a = 10
b = 7

result = "a가 b보다 큽니다" if a > b else "b가 a보다 큽니다." 
print(result)




# match~case문

# 문자열
subject = input("과목을 입력해주세요 >>> ")

match subject:
    case "국어":
        print("1교시 입니다.")
    case "수학":
        print("2교시 입니다")
    case "과학":
        print("3교시 입니다")
    case _:                                  # 와일드카드
        print("유효하지 않는 과목입니다")


# 문자열 관련 함수 
user_input = input("Enter a fruit >>> ")

match user_input.lower():                   # lower() -> 대문자를 소문자로 변환,  upper() -> 소문자를 대문자로 변환 
    case "apple":
        print("Apple is red.")
    case "banana":
        print("Banana is Yellow.")
    case "cherry":
        print("Cherry is red.")    


