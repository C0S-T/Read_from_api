import read_data_from_city
import os
import requests

FOLDER = 'read_from_api/'
CORDINATES_OF_CITY_FOLDER = 'outputs.txt'

BASE_URL_OF_COORD = 'api.openweathermap.org/data/2.5'
API_KEY = '3b66f592d458664efde58a8fda5dc3e4'


cordinates_lists = read_data_from_city.get_city_cordinates()
#print(cordnates_list)
os.remove(FOLDER+CORDINATES_OF_CITY_FOLDER)
read_data_from_city.write_in_file(FOLDER+CORDINATES_OF_CITY_FOLDER,cordinates_lists)