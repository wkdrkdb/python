try:
    numerator = int(input("첫 번째 숫자를 입력하세요: "))
    denominator = int(input("두 번째 숫자를 입력하세요: "))
    result = numerator / denominator

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자를 입력해 주세요!")
else:
    print("나누기 결과: ", result)