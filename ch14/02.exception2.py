# 변수를 선언합니다.
list_input_a = ["52", "273", "32", "스파이", "103"]

# 반복문을 적용합니다

list_number = []

for item in list_input_a:
    try:
        item = float(item)
        list_number.append(item)
    except:
        pass

# 출력합니다
print(f"{list_input_a} 중에서 숫자만 추출하면 {list_number}입니다.")    