import requests
## pip3 install requests

APPID = '67da29cb91129f1a68c1c06c1be92daa' # use your own APPID
CITY = 'London'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&units=imperial&appid={APPID}"

def get_weather_data():
    # envia un HTTP GET al URL
    response = requests.get(URL) # get devuelve un object (propiedades + metodos realizables en ese objeto)
    # print(response, type(response))
    hhtp_response_code = response.status_code
    data = response.json() # el metodo json() nos permite leer los datos de la response

    # print(hhtp_response_code, type(hhtp_response_code))
    # print(data, type(data))

    # retun tuple con dos valores status code, data
    return response.status_code, response.json()


def main():
    response =  get_weather_data()
    status_code, data =  response
    print (status_code, data, sep='\n')


main()