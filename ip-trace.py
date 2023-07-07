import requests
import folium

ip = input("Masukkan IP: ")
url = f"https://ipapi.co/{ip}/json"

r = requests.get(url)
data = r.json()

latitude = float(data['latitude'])
longitude = float(data['longitude'])

# Membuat objek peta menggunakan folium
m = folium.Map(location=[latitude, longitude], zoom_start=10)

# Menandai lokasi pada peta
folium.Marker([latitude, longitude], popup=f"IP: {ip}").add_to(m)

# Menampilkan peta
m.save('map.html')
