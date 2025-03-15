import random

# 전달하는 두 인수를 포함한 사이의 정수를 임의로 생성하는 함수 
res = random.randint(1, 45)
print(res)

print("------------------------------------------------------")

# 전달하는 두 인수 중 마지막 숫자를 제외한 나머지 정수를 임의로 생성하는 함수 
res = random.randrange(1, 45)
print(res)

print("------------------------------------------------------")

# 0 이상 1미만의 범위에서 실수를 생성하는 함수
res = random.random()
print(res)

if res < 0.5:
    print(f"가유의 전설의 검을 획득했습니다!(확률: {int(res * 100)}%)") 
else:
    print(f"확률: {int(res * 100)}%")

print("------------------------------------------------------")

items = ['전설의 검', '날이 무딘 검', '칼자루만 남은 검', '칼집']
random.shuffle(items)
print(items)

print("------------------------------------------------------")

res = random.choice(items)
print(res)