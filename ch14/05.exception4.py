# try - except 구문으로 예외를 처리합니다.

try:
    # 사용자로부터 입력을 받습니다.
    number_input = int(input("정수 입력(반지름): "))
    
    # 출력합니다
    print("원의 반지름: ", number_input)
    print("원의 둘레: ", 2 * 3.14 * number_input)
    print("원의 넓이: ", 3.14 * number_input ** 2)

except Exception as exception:
    # 예외가 발생하면 실행되는 코드 
    # print("예외가 발생했습니다.")
    print(f"type(exception): {type(exception)}")
    print(f"exception: (exception)")

print("-------- 프로그램 종료 --------")