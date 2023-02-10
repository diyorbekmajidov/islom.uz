from bs4 import BeautifulSoup
import requests

# url = f'https://islom.uz/'

# def namoz_vaqtlari():
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')  
#     bomdod = soup.find('div', id = "tc1").text
#     quyosh = soup.find('div', id = "tc2").text
#     peshin = soup.find('div', id = "tc3").text
#     asr = soup.find('div', id = "tc4").text
#     shom = soup.find('div', id = "tc5").text
#     xufton = soup.find('div', id = "tc6").text

#     return bomdod,quyosh,peshin,asr,shom,xufton

def prayer(city):
	url = "https://aladhan.p.rapidapi.com/timingsByCity"

	querystring = {"country":"Uzbekistan","city":"Smarkand"}

	headers = {
		"X-RapidAPI-Key": "985cef3375msh3d3b11fac985565p1acdc4jsnbb0709f31f0b",
		"X-RapidAPI-Host": "aladhan.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	data = response.json()
	fajr = data["data"]["timings"]["Fajr"]
	sunrise = data["data"]["timings"]["Sunrise"]
	dhuhr = data["data"]["timings"]["Dhuhr"]
	asr = data["data"]["timings"]["Asr"]
	sunset = data["data"]["timings"]["Sunset"]
	maghrib = data["data"]["timings"]["Maghrib"]
	isha = data["data"]["timings"]["Isha"]
	imsak = data["data"]["timings"]["Imsak"]
	midnight = data["data"]["timings"]["Midnight"]
	firstthird = data["data"]["timings"]["Firstthird"]
	lastthird = data["data"]["timings"]["Lastthird"]
	print(fajr,sunrise,dhuhr,asr,sunset,maghrib,isha,imsak,midnight,firstthird,lastthird)

# if __name__ == '__main__':
#     namoz_vaqtlari()

# print(namoz_vaqtlari())