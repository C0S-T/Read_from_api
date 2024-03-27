import requests
# import json

#constants
BASE_URL_OF_COORD = 'api.openweathermap.org/data/2.5'
API_KEY = '3b66f592d458664efde58a8fda5dc3e4'

#LOCATION = 'hyderabad,in'
#URL = f'https://{BASE_URL_OF_COORD}//weather?appid={API_KEY}&q={LOCATION}&units=metric'
FOLDER = 'read_from_api/'
FILE_NAME_OF_CITIES = 'list_of_locations.txt'
CORDINATES_OF_CITY_FOLDER = 'outputs.txt'

#open file of city name and read through url to get lati,longi and store is dict
def  get_city_cordinates():
    with open(FOLDER+FILE_NAME_OF_CITIES, 'r') as file: 
        #convert the str in the file into list [locations] of strings
        locations = file.read().strip().split('\n')
        #print(locations)
        city_cord_list = []
        for city in locations:
            url = f'https://{BASE_URL_OF_COORD}//weather?appid={API_KEY}&q={city}&units=metric'
            data_of_city = requests.get(url)
            if(data_of_city.status_code == 200):
                longitude = data_of_city.json()["coord"]["lon"]
                latitude = data_of_city.json()['coord']['lat']
                #print(longitude, latitude)
                #check for duplicacy and append in dict
                p = get_city_weather(str(latitude),str(longitude))
                if city not in city_cord_list:
                    data = f'{city},{latitude},{longitude},{p}'
                else:
                    data = f'{city} not found in server'
                city_cord_list.append(data)
            else:
                print(city,' Failed to fetch data from OpenWeatherMap API server')
    return city_cord_list

#write the dictionary (city_corinated) into a text file(output_file_name)
def write_in_file(output_file_name,city_cord_list):
    with open(FOLDER+CORDINATES_OF_CITY_FOLDER, 'a') as file:
        file.write('city,latitute,longitude,(dt,temp_min,temp_max,humidty) : \n')
        for city in city_cord_list:
            file.write(str(city) + '\n')


def get_city_weather(latitude,longitude):
    url_for_weather = f'https://{BASE_URL_OF_COORD}/forecast?appid={API_KEY}&lat={latitude}&lon={longitude}'
    parameters = requests.get(url_for_weather)
    # print(parameters.status_code)
    temp_min = parameters.json()['list'][0]['main']['temp_min']
    temp_max = parameters.json()['list'][0]['main']['temp_max']
    humidity = parameters.json()['list'][0]['main']['humidity']
    dt = parameters.json()['list'][0]['dt']
    #id = parameters.json()['list'][39]["city"]["id"]
    #print(len(list))
    return dt,temp_min,temp_max,humidity #,id
    