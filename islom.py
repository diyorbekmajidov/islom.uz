from bs4 import BeautifulSoup
import requests

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
	sunset = data["data"]["timings"]["Sunset"]
	maghrib = data["data"]["timings"]["Maghrib"]
	isha = data["data"]["timings"]["Isha"]
	imsak = data["data"]["timings"]["Imsak"]
	midnight = data["data"]["timings"]["Midnight"]
	firstthird = data["data"]["timings"]["Firstthird"]
	lastthird = data["data"]["timings"]["Lastthird"]
	
	return {"fajr":fajr,"sunrise":sunrise,"dhuhr":dhuhr,"asr":asr,"sunset":sunset,"maghrib":maghrib,"isha":isha,"imsak":imsak,"midnight":midnight,"firstthird":firstthird,"lastthird":lastthird}

