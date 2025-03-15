def find_max_min_value(numbers: list) -> list:       # 여러개의 정수를 전달받아서 최대값과 최소값을 반환하는 함수를 정의하세요.
    """
    이 함수는 리스트를 매개변수로 받아서 최대값과 최소값을 구하는 함수입니다.
    """

    # 최대값과 최소값 찾는 방법
    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers:      # 대소 비교
        if number > max_value:
            max_value = number

        if number < min_value:
            min_value = number

    return [max_value, min_value] 

result = find_max_min_value([1, 4, 2, 65, 7, 87])           
print(result[0])    # 최대값
print(result[1])    # 최소값