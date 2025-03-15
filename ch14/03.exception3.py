# try-exception-else

try:
    number_input = int(input("숫자를 입력하세요: "))
except:
    print("정수를 입력하지 않았습니다.") 
else:
    print("원의 반지름", number_input)       
    print("원의 들레", 2 * 3.14 * number_input)     

# --------------------------------------------------------------
print()


x = "문자"

try:
    int(x)
    print("try 구문 실행")
except:
    print("예외 발생! except 구문 실행")
else:
    print("정상 실행! else 구문 실행")
finally:    # 예외 발생과 상관없이 무조건 실행되는 코드 
    print("try 구문 실행완료! finally 구문 실행")            
