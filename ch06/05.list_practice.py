# 다음은 A반의 학생들의 명단입니다. 각 문제에 맞는 코드를 작성하세요.
class_a = ["현우", "지영", "동혁"]

# 문제1 
# A반에 상준이가 전학을 왔습니다. 명단을 추가해주세요. (마지막)
class_a.append("상준")
print(class_a)

# 문제2
# "현우"가 "현석"으로 개명했습니다. 이름을 수정하세요.
"""
class_a[0] = "현석"
print(class_a)
"""
result = class_a.index("현우")
print(result)
class_a[result] = "현석"
print(class_a)

# 문제3
# 이번주 청소 당번은 지영이랑 동혁입니다. "슬라이싱"을 사용해서 청소 당번을 출력하는 코드를 작성하세요.
print(class_a[1:3])

# 문제4
# 이번주 우유 당번은 명단의 마지막 학생입니다. "음수 인덱스"를 사용하여 우유 당번을 출력하세요.
print(class_a[-1])



class_a = ["현우", "지영", "동혁"]
class_b = ["삼영", "재석", "기영", "영자"]

# 문제5
# 기존의 A반"에" B반 학생들을 합치기로 했습니다. 합치는 코드를 작성하세요.
class_a.extend(class_b)
print(class_a)

# 문제6
# 합쳐진 A반 학생들을 이름순(오름차순)으로 정렬하세요.
class_a.sort()
print(class_a)

# 문제7
# 동혁이가 다른 학교 전학을 갔습니다. 학생 명단에서 제거해주세요. (값으로 제거)
class_a.remove("동혁")
print(class_a)
