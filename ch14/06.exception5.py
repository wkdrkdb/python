# 변수를 선언합니다
numbers = [52, 273, 18, 38, 100]

# try - exception 구문으로 예외를 처리합니다
try:
    # 숫자를 입력받습니다.
    number_input = int(input("정수 입력: "))
    
    # 리스트의 요소를 출력합니다.
    print(f"{number_input}번째 요소: {numbers[number_input]}")
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print(f"exception: {exception}")
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")    
    print(f"exception: {exception}")
except Exception as exception:
    print(f"exception: {exception}")



"""
except Exception as exception:
    print(f"type(exception): {type(exception)}")
    print(f"exception: {exception}")

# 리스트의 인덱스를 벗어날시 IndexError
# 문자열 입력시 ValueError    

"""
