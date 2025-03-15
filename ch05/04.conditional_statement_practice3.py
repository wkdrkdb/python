first_number = int(input("첫 번째 숫자를 입력해주세요 >>> "))
second_number = int(input("두 번째 숫자를 입력해주세요 >>> "))
third_number = int(input("세 번째 숫자를 입력해주세요 >>> "))

"""
if (first_number > second_number) and (first_number > third_number):
    print(f"가장 큰 수는 {first_number} 입니다.")
elif (second_number > first_number) and (second_number > third_number):
    print(f"가장 큰 수는 {second_number} 입니다.")
else:
    print(f"가장 큰 수는 {third_number} 입니다.")    
"""

if (first_number > second_number) and (first_number > third_number):
    max_number = first_number
elif (second_number > first_number) and (second_number > third_number):
    max_number = second_number
else:
    max_number = third_number

print(f"가장 큰 수는 {max_number} 입니다.")    