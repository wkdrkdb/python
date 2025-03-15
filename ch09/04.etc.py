# len() 데이터 길이
text = "Hello, World!"
print(len(text))


# abs() 절대값
result = abs(-10)
print(f"abs() 절대값: {result}")


# format() 문자 포맷관련 함수
result = format(1000)           # str(1000) 같다
result = format(100000, ",")    # 천단위 "," 표시
print(f"format(100000, ',') : {result}")


# max() 최대값 반환
result = max(1, 10)
print(f"max(1, 10) : {result}")


# min() 최소값 반환
result = min([5, 3, 7, 8, 2, 9])
print(f"min([5, 3, 7, 8, 2, 9]) : {result}")


# pow() 거듭제곱 함수
result = pow(10, 2)
print(f"pow(10, 2) : {result}")


# sorted() 함수 - 정렬
my_li = [5, 6, 3, 4, 1, 2]
result = sorted(my_li)
print(f"sorted(my_li) : {result}")


# 역정렬 
result = sorted(my_li, reverse=True)
print(f"sorted(my_li, reverse=True) : {result}")


# zip() 함수 - 같은 인덱스 번호끼리 튜플로 묶어 줍니다.
names = ["james", "emily", "amanda"]
scores = [60, 70, 80]
for student in zip(names, scores):
    print(student)
     

for name, score in zip(names, scores):
    print(f"{name}의 점수는 {score}점 입니다.")




