# CSV 파일 읽기

# 콤마로 구분된 문자열을 리스트로 반환 
alphabets = "a, b, c, d, e"

result = alphabets.strip().split(',')    # .split(',')  ->  , 를 기준으로 분리 
print(result)   


print("-----------------------------------------------------------------------------------")
# 회원정보.csv 파일 읽기
members = []
with open('./회원정보.csv', 'rt', encoding='utf-8') as file:
    data = file.readlines()
    for line in data:
        member = line.strip().split(',')
        members.append(member)

print(members)

print("-----------------------------------------------------------------------------------")
# 변환된 데이터를 사용해서 이름 데이터만 추출하기 
names = []
for member in members[1:]:
    names.append(member[2])

print(names)