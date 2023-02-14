from bs4 import BeautifulSoup
import requests
import main

def prayer(city):
	url = "https://aladhan.p.rapidapi.com/timingsByCity"

	querystring = {"country":"Uzbekistan","city":f"{city}"}

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
	asr1 = f'{int(asr.split(":")[0])+1}:{asr.split(":")[1]}'
	sunset = data["data"]["timings"]["Sunset"]
	maghrib = data["data"]["timings"]["Maghrib"]
	isha = data["data"]["timings"]["Isha"]
	imsak = data["data"]["timings"]["Imsak"]
	midnight = data["data"]["timings"]["Midnight"]
	firstthird = data["data"]["timings"]["Firstthird"]
	lastthird = data["data"]["timings"]["Lastthird"]
	main.text_to_image(city,fajr,sunrise,dhuhr,asr1,maghrib,sunset,isha,midnight,"Ubuntu-Medium.ttf", 30, (251,240,147))
	# return {"fajr":fajr,"sunrise":sunrise,"dhuhr":dhuhr,"asr":asr,"sunset":sunset,"maghrib":maghrib,"isha":isha,"imsak":imsak,"midnight":midnight,"firstthird":firstthird,"lastthird":lastthird}
# print(prayer("Tashkent"))