from bs4 import BeautifulSoup
import requests
from main import text_to_image


# parser url 
def Namozregion():
    url ='https://islom.uz/region/1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    regions = soup.find('div', class_ = "custom-select")
    print(regions)
    region = {"region_name":[]}
    k=0
    for i in regions.find('select').find_all('option'):
        k = +1
        region["region_name"].append({f'{i.text}':i['value']})
    return region


def parser_url(city):
	data ={'region_name': 
    {'Андижон': '1', 'Бухоро': '4', 'Гулистон': '5',  
    'Навоий': '14', 'Наманган': '15', 'Нукус': '16', 
    'Самарқанд': '18', 'Термиз': '74', 'Тошкент': '27',  
    'Фарғона': '37',  'Хива': '21',  'Қарши': '93', 
    'Қарши': '25'}
    }

	url = f'https://islom.uz/region/{data["region_name"][city]}'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	bomdod = soup.find('div', id = "tc1").text
	quyosh = soup.find('div', id = "tc2").text
	peshin = soup.find('div', id = "tc3").text
	asr = soup.find('div', id = "tc4").text
	shom = soup.find('div', id = "tc5").text
	xufton = soup.find('div', id = "tc6").text

	text_to_image("Samarqand",bomdod, quyosh, peshin, asr, shom, xufton, "Ubuntu-Medium.ttf", 30, (251,240,147))

# print(parser_url())



