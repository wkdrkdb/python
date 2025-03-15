"""
✅ 문제
다음 빈칸을 채워서 사용자로부터 입력받아 “Todo List”를 다음과 같이 출력하는 프로그램을 완성하세요.

<실행 결과>

할 일 목록(1): 운동하기
할 일 목록(2): 파이썬 복습하기
할 일 목록(3): 샤워하기
할 일 목록(4): 독서하기

"""

todo_list = []
user_input = ""

while user_input.lower() != "quit":
    user_input = input("TODO List를 입력하세요. (종료하려면 'quit') >>> ")
    if user_input.lower() != "quit":
        todo_list.append(user_input)

count = 1
for todo in todo_list:
    print(f"할 일 목록({count}): {todo}")
    count += 1
