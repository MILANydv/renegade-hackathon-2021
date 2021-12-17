import urllib.request
import json
from django.shortcuts import render


# Create your views here.
def form(request):
    return render(request, 'home/form.html')


# import json to load json data to python dictionary
# urllib.request to make a request to api


def Homepage(request):

    if request.method == 'POST':
        city = request.POST['city']

        # source contain JSON data from API

        start_url = "https://api.openweathermap.org/data/2.5/weather?q= { city }&appid={fa84278949b90d5ec1f082b8c0ba3fb8}"
        # start_url = 'https://api.openweathermap.org/data/2.5/weather?q = {city } & appid = {API key}'
        url = start_url.replace(" ", "")
        source = urllib.request.urlopen(url).read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
            + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "home/homepage.html", data)
