# oop(Object Oriented Programing)

# 객체지향 프로그래밍이란: 객체를 중심으로 개발하는 방법론
# 객체란: 현실에 존재하는 특정 대상을 소프트웨어 내부에서 사용할 수 있도록 개념적으로 정의한 것
# 클래스란: 개념으로 정의된 특정 대상을 문서화한 것

# 클래스가 왜 필요한가?
#   딕셔너리 + 리스트 = 학생관리프로그램에 필요한 데이터

students = [{
    "name" : "옥순",
    "korean" : 87,
    "math" : 98,
    "english" : 88,
    "science" : 90
},

{
    "name" : "영수",
    "korean" : 87,
    "math" : 98,
    "english" : 88,
    "science" : 90
},

{
    "name" : "영철",
    "korean" : 87,
    "math" : 98,
    "english" : 88,
    "science" : 90
},

{   "name" : "순자",
    "korean" : 87,
    "math" : 98,
    "english" : 88,
    "science" : 90
}    
]


print("이름", "총점", "평균", sep='\t')
for student in students:
    # 점수의 총합과 평균 구하기
    sum = student["korean"] + student["math"] + student["english"] + student["science"]
    average = sum / 4
    print(student["name"], sum, average, sep='\t') 