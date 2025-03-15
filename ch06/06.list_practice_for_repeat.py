"""
A반 학생들의 턱걸이 횟수를 입력받고 학습 평균을 구하는 간단한 프로그램을 만들어 보겠습니다. 
아래의 형식에 맞게 표준입력함수로 턱걸이 횟수 를 입력받고 평균 턱걸이 횟수를 계산하여 
소수점 첫 번째 자리에서 반올림하여 표준출력과 동일하게 print문 을 작성하시기 바랍니다.

"""

record = []

count = int(input("현우의 턱걸이 횟수를 입력해주세요 >>> "))
record.append(count)
count = int(input("지영이의 턱걸이 횟수를 입력해주세요 >>> "))
record.append(count)
count = int(input("동혁이의 턱걸이 횟수를 입력해주세요 >>> "))
record.append(count)
count = int(input("상준이의 턱걸이 횟수를 입력해주세요 >>> "))
record.append(count)

# total = record[0] + record[1] + record[2] + record[3]
total = sum(record)
print(total)

average = total / len(record)
print(round(average))

