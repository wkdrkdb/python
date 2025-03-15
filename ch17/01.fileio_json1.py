# JSON 형식 파일

import json

FILE_PATH = './member.Json'

members = [
    {
        "member_no" : 1,
        "member_id" : "oksoon",
        "member_name" : "옥순",
        "member_phone_number" : "010-111-1234"
    },
    {
        "member_no" : 2,
        "member_id" : "soonja",
        "member_name" : "순자",
        "member_phone_number" : "010-222-1234"
    }
]

with open(FILE_PATH, 'w', encoding='utf-8') as file:
    json.dump(members, file, indent=4, ensure_ascii=False) 

print('member.json 파일이 생성되었습니다')  



with open(FILE_PATH, 'r', encoding='utf-8') as file:
    json_reader = file.read()
    print(type(json_reader))    # str
    members = json.loads(json_reader)
    print(type(members))        # list

    for member in members:
        print(f"회원번호: {member['member_no']}")
        print(f"아이디: {member['member_id']}")
        print(f"이름: {member['member_name']}")
        print(f"전화번호: {member['member_phone_number']}")
        print()

