from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language= "ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            return lat, lon
        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка {e}"


key = 'ecf8491258f748f791992d713ce185c2'
city = "Санкт-Петербург"
coordinates = get_coordinates(city, key)

print(f"Координаты города {city}: {coordinates}")