import requests
import pprint

ip = "(isi ipmu)"
url = f"https://ipapi.co/{ip}/json"

r = requests.get(url)
pprint.pprint(r.json())
