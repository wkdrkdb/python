# csv 모듈

import csv

# csv 모듈로 파일 쓰기 
with open('./상품관리.csv', 'wt', newline='', encoding='utf-8') as file:
    csv_maker = csv.writer(file)
    csv_maker.writerow(['상품명', '가격', '수량'])
    csv_maker.writerow(['사과', 1000, 10])
    csv_maker.writerow(['딸기', 2000, 5])

    print('상품관리.csv 파일이 생성되었습니다.')

# csv 모듈로 파일 읽기
with open('./상품관리.csv', 'rt', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',', quotechar='"')
    print(csv_reader)

    for line in csv_reader:
        print(line)

print('----------------------------------------------------------------------')

# 상품명만 추출하는 코드 작성
with open('./상품관리.csv', 'rt', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    product_names = []
    next(csv_reader) # 첫번째 줄 제외 -> 상품종류에서 '상품명' 제외
    for line in csv_reader:
        # 수량이 10개 미만인 상품만 product_names에 추가 
        if int(line[2]) < 10:
            product_names.append(line[0])

print(f"상품종류: {product_names}")