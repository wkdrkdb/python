import requests

"""
geocoding API로 받아온 위도/경도 정보를 weather_service.py의 get_weather_data 함수로 전달 
"""

def get_geocoding_data(city: str):

    from weather_service import get_weather_data
    
    print("Hello get_geocoding_data")

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=c0b2092f9bae7f65190f113604e751f7"

    response = requests.get(url=url)
    data = response.json()
    print(response)
    
    lat = data[0].get('lat')
    lon = data[0].get('lon')

    print("=============>", lat, lon)
    get_weather_data(lat, lon)

if __name__ == "__main__":
    city = input("지역/나라 이름: ")
    get_geocoding_data(city)
