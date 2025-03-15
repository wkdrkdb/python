"""
enumerate() 함수
    List, Tuple, String 등 자료형을 입력 받으면
    인덱스 값을 포함하는 enumerate 객체를 돌려준다.
"""

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month, day in enumerate(months, start=1):
    print(f"{month}월 = {day}")

    