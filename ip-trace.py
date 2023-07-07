import requests
import pprint

ip = input("Masukkan IP: ")
url = f"https://ipapi.co/{ip}/json"

r = requests.get(url)
pprint.pprint(r.json())

