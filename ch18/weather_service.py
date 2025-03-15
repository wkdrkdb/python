# 날씨 정보를 제공하는 모듈 
# open weather api
# postman

import requests
import datetime

def get_weather_data(lat: str, lon: str):
    print("Hello get_weather_data")
    print(lat, lon)
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid=c0b2092f9bae7f65190f113604e751f7&units=metric&lang=kr"

    # API 요청 보내기 
    response = requests.get(url=url)
    data = response.json()
    print(response)
    # print(data)

    # 현재 날씨 정보 출력 
    current = data.get('current', {})
    print("현재 날씨 정보")
    print(f"온도 : {current.get('temp')}도")
    print(f"체감 온도: {current.get('feels_like')}도")
    print(f"습도 : {current.get('humidity')}%")
    # print(f"구름 상태: {current.get('weather')[0].get('description')}")


    """ 구름 정보 추출
    weather = current.get('weather')
    weather_data = weather[0]
    description = weather_data.get('description')
    print(f"구름 상태: {description}")
    """

    print("======================================================================")

    # 시간별 예보 가져오기 
    #   hourly 리스트 중 4번 인덱스까지만 데이터 추출 아래 정보 출력 

    print("시간별 날씨 예보")
    for hourly in data.get('hourly', [])[:5]:
        dt = datetime.datetime.fromtimestamp(hourly.get('dt'))
        print(f"시간: {dt}")
        print(f"온도: {hourly.get('temp')}")
        print(f"체감 온도: {hourly.get('feels_like')}")
        print(f"구름 상태: {hourly.get('weather')[0].get('description')}")
        print(f"강수 확률: {hourly.get('pop') * 100}%")
        print()



    """
    hourly = data.get('hourly', [])

    print("시간별 날씨 예보")

    i = 0
    while i < 5:
        data = hourly[i]
        dt = datetime.datetime.fromtimestamp(data.get('dt'))
        print(f"시간: {dt}")
        print(f"온도: {data.get('temp')}도")
        print(f"체감 온도: {data.get('feels_like')}도")
        print(f"구름 상태: {data.get('weather')[0].get('description')}")
        print(f"강수 확률: {data.get('pop') * 100}%")
        print()
        i += 1
    """



    print("======================================================================")

    # 일간 예보 가져오기 
    #   daily 리스트 중 4번 인덱스까지만 데이터 추출 아래 정보 출력
    print("일간별 날씨 예보")

    for daily in data.get('daily', [])[:5]:
        dt = datetime.datetime.fromtimestamp(daily.get('dt'))
        sunrise = datetime.datetime.fromtimestamp(daily.get('sunrise'))
        sunset = datetime.datetime.fromtimestamp(daily.get('sunset'))
        
        print(f"시간: {dt}")
        print(f"일출 시간: {sunrise}")
        print(f"일몰 시간: {sunset}")
        print(f"최고 기온: {daily.get('temp').get('max')}도")
        print(f"최저 기온: {daily.get('temp').get('min')}도")
        print(f"강수 확률: {daily.get('pop') * 100}%")
        print()


    """
    조회된 날씨 정보를 출력하는 open_weather_result_window(현재 온도, 체감 온도, 현재 습도) 호출
    """
    from screen import open_weather_result_window
    open_weather_result_window(
        temp=current.get('temp'),
        feels_like=current.get('feels_like'),
        humidity=current.get('humidity')
    )

    
if __name__ == "__main__":
    lat = input("위도: ")
    lon = input("경도: ")
    get_weather_data(lat, lon)