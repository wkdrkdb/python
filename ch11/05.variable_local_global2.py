# 전역변수를 함수에서 사용하는 예시 

total = 0

def gift(dic, who, money):
    global total            # 함수 내부에서 전역변수 total 사용하겠다 선언
    total += money          # 전역변수 total에 money 값 더함
    dic[who] = money        # 딕셔너리 dic에 누구(who)가 얼마(money)를 낸 기록 저장 


wedding = {}                # 축의금 기록을 저장할 딕셔너리
name = "영희"

# 함수 호출하여 축의금 기록 
gift(wedding, name, 5)      
gift(wedding, "철수", 6)
gift(wedding, "이모", 10)

print(f"축의금 명단 : {wedding}")
print(f"전체 축의금 : {total}")

