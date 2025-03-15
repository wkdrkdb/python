""""
break 문
    while문이나 for문과 같은 반복문을
    강제로 종료하는 제어문 
"""

n = 1
while True:             # while True -> 무한반복
    print(n)
    if n == 10:
        break

    n += 1

print("while end")