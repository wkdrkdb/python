name = input("학생의 이름을 입력해주세요 >>> ")
korean = int(input("국어 점수를 입력해주세요 >>> "))
english = int(input("영어 점수를 입력해주세요 >>> "))
math = int(input("수학 점수를 입력해주세요 >>> "))


subject = ""
score = 0

if not(0 <= korean <= 100):
    subject = "국어"
    score = korean
elif not(0 <= english <= 100):
    subject = "영어"
    score = english
elif not(0 <= math <= 100):
    subject = "수학"
    score = math

if subject == "" :
    average = (korean + english + math) / 3

    if average >= 80:
        print("보충학습 대상 학생이 아닙니다.")
    else:
        differ = 80 - average
        print(f"{name}: 보충학습 대상 학생입니다. (점수차: {round(average)})")       # round() -> 반올림 , round(~~~, 2) -> 소수점 2번째 자리까지 표현(소수점 3번째 자리에서 반올림) 
else : 
    print(f"{name}: {subject} 점수 입력 오류입니다. 입력값: ({score})")    
