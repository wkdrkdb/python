number = int(input("숫자를 입력해주세요 >>> "))

if number == 0:
    print("입력하신 숫자는 0 입니다.")
elif number % 2 == 0:
    print("입력하신 숫자는 짝수입니다.")
else:
    print("입력하신 숫자는 홀수입니다.")