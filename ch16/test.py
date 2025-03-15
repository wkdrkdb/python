# 서울교통공사_승하차인원.csv 파일을 활용한 데이터 추출

# 문제(1) : csv.reader를 사용해서 CSV 파일을 읽고 각 행의 데이터를 출력하는 프로그램을 완성하세요.
# 예시출력
#   연월: 2023-01, 역명: 서울역(1), 승하차인원수: 2744112

import csv

    

with open('./서울교통공사_승하차인원.csv', 'rt', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    transport_date_index = header.index("수송연월")
    station_name_index = header.index("역명")
    passenger_count_index = header.index("승하차인원수")

    max_passenger_count = 0
    max_station = ""
    monthly_max_stations = {}

    for row in csv_reader:
        transport_date = row[transport_date_index]
        station_name = row[station_name_index]
        passenger_count = int(row[passenger_count_index])

        print(f"연월: {transport_date}, 역명: {station_name}, 승하차인원수: {passenger_count}")


# ------------------------------------------------------------------------------------------------------------

# 문제(2)
#   2023-01 월에 승하차 인원이 가장 많은 역의 이름과 그 승하차 인원수를 출력하는 프로그램을 완성하세요.
#   if 문을 사용하여 특정 월(2023-01)에만 해당하는 데이터를 필터링하고, 승하차 인원수를 비교해  
#   가장 큰 값을 가진 역 이름을 찾으세요          
# 예시 출력
#   2023-01월에 가장 많은 승하차 인원을 가진 역: 서울역(1) (2744112명)

        if (transport_date == "2023-01") and (passenger_count > max_passenger_count):
            max_station = station_name
            max_passenger_count = passenger_count

# print(f"2023-01월에 가장 많은 승하차 인원을 가진 역: {max_station} ({max_passenger_count}명)")


# ------------------------------------------------------------------------------------------------------------

# 문제(3)
#   각 월마다 최대 승하차 인원을 가진 역을 찾아 저장하는 프로그램을 완성하세요.
#   각 월에 대해 최대 승하차 인원과 그 역 이름을 저장하기 위한 monthly_max_stations 라는 빈 딕셔너리를 선언하세요.
#   monthly_max_stations 딕셔너리에는 각 달을 키(key)로, 해당 달에 승하차 인원/역명 저장합니다.
# 예시 출력
#   2023-01: 서울역(1) (2744112명)
#   2023-02: 종각 (1994694명)

        if (
            transport_date not in monthly_max_stations
            or passenger_count > monthly_max_stations[transport_date]["passenger"]
        ):
            monthly_max_stations[transport_date] = {
                "station" : station_name,
                "passenger" : passenger_count
            }

for month, data in monthly_max_stations.items():
    print(f"{month}: {data["station"]} ({data["passenger"]}명)")



































