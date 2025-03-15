import random
from send_mail import send_mail

    # Ver1 (중복값 O)

#    numbers = []

#    while len(numbers) < 6:
#        number = random.randint(1, 45)
        
        # numbers에 해당 숫자가 존재하는지 확인
#        if number not in numbers:
#            numbers.append(number)

#    print(numbers)

#    print("====================================================")




# Ver 2 (중복값 X)
def create_lotto_numbers():
    numbers = set()

    while len(numbers) < 6:
        number = random.randint(1, 45)
        numbers.add(number)

    # set -> list
    numbers = list(numbers)
    # print(numbers)

    message = f"""
    [당첨되면 반띵]

    첫번째 번호: {numbers[0]}
    두번째 번호: {numbers[1]}
    세번째 번호: {numbers[2]}
    네번째 번호: {numbers[3]}
    다섯번째 번호: {numbers[4]}
    여섯번째 번호: {numbers[5]}
    """

    send_mail(
        'gayou20065@gmail.com',
        '[로또 번호가 궁금하십니까?] 눌러보세요!',
        message
    )