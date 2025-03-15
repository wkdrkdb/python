import json


def load_data_fromjson(file_path: str):
    """
    이 함수는 데이터를 JSON 파일로 저장합니다.
    """

    with open(file_path, 'r') as file:
        json_reader = file.read()
        data = json.loads(json_reader)
    return data

def save_data_tojson(file_path: str, data):
    """
    이 함수는 데이터를 JSON 파일로 저장합니다.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f'{file_path}에 파일이 생성되었습니다.')