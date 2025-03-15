name = input("학생의 이름을 입력해주세요 >>> ")
score1 = int(input("국어 점수를 입력해주세요 >>> "))
score2 = int(input("영어 점수를 입력해주세요 >>> "))
score3 = int(input("수학 점수를 입력해주세요 >>> "))


if (score1 < 0) or (score1 > 100):
    print(f"{name}: 국어 점수 입력 오류입니다. (입력값: {score1})")
elif (score2 < 0) or (score2 > 100):
    print(f"{name}: 영어 점수 입력 오류입니다. (입력값: {score2})")
elif (score3 < 0) or (score3 > 100):
    print(f"{name}: 수학 점수 입력 오류입니다. (입력값: {score3})")

"""
or 대신 not도 사용가능  

if not(0 <= score1 <= 100):
    print(f"{name}: 국어 점수 입력 오류입니다. (입력값: {score1})")  
"""    


score4 = 80 - ((score1 + score2 + score3) / 3)

if ((score1 + score2 + score3) / 3) > 80:
    print(f"{name}: 보충학습 대상 학생이 아닙니다.")
else:
    print(f"{name}: 보충학습 대상 학생입니다. (점수차: {round(score4)})")       # round() -> 반올림 , round(~~~, 2) -> 소수점 2번째 자리까지 표현(소수점 3번째 자리에서 반올림) 




"""
average = (score1 + score2 + score3) / 3
if average >=  80:
    print("보충학습 대상이 아닙니다.")
else:
    differ = 80 - average
    print(f"보충학습 대상 학생입니다 (점수차 : {round(differ)})")    
"""


