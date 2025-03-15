# 숫자를 입력 받습니다
number_input = input("숫자를 입력하세요: ")

print(number_input.isdigit())

# 조건문을 사용한 예외처리
# 숫자형 데이터인지 검증합니다.
if number_input.isdigit():
    number_input = int(number_input)
    # 출력합니다
    print("원의 반지름: ", number_input)
    print("원의 둘레: ", 2 * 3.14 * number_input)
    print("원의 넓이: ", 3.14 * number_input * number_input)

print("==================================================")



# try-except 구문을 사용한 예외처리
try:
    number_input = int(input("숫자를 입력하세요: "))
    print("원의 반지름: ", number_input)
    print("원의 둘레: ", 2 * 3.14 * number_input)
    print("원의 넓이: ", 3.14 * number_input * number_input)    
except:
    print("무언가 잘못되었습니다.")

print("프로그램이 종료되었습니다.")    