def create_student(name, korean, math, english, science):
    student = {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    } 
    return student

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4     # student_get_sum(student) / (len(student)-1) -> 더 유연하다.

students = [
    create_student("옥순", 87, 98, 88, 90),
    create_student("영수", 87, 98, 88, 90),
    create_student("영철", 87, 98, 88, 90),
    create_student("순자", 87, 98, 88, 90)
]

print("이름", "평균", sep='\t')
for student in students:
    average = student_get_average(student)
    print(student["name"], average, sep='\t') 
