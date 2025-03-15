from datetime import datetime          

year = int(input("태어난 연도를 입력하세요 >>> "))
age = (datetime.now().year) - year                  # (datetime.now().year) 올해 년도 . 그냥 2024 - year 해도 됨. 

print(f"현재 나이는 {age}세 입니다.")

