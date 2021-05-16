from django.shortcuts import render
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': str(os.getenv('COVID-APIKEY')),
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
response = requests.get(url, headers=headers).json()

def home(request):
    noofresults = int(response['results'])
    list = []
    for i in range(0,noofresults):
        list.append(response['response'][i]['country'])
        list.sort()
    if request.method == "POST":
        selectedcountry = request.POST["selectedcountry"]
        for i in range(0,noofresults):
            if (selectedcountry == response['response'][i]['country'] ):
                new = response['response'][i]['cases']['new']
                active = response['response'][i]['cases']['active']
                critical = response['response'][i]['cases']['critical']
                recovered = response['response'][i]['cases']['recovered']
                total = response['response'][i]['cases']['total']
                deaths = int(total)-int(active)-int(recovered)

        context = {
        'new' : new ,
        'active':active,
        'critical' : critical,
        'recovered' : recovered ,
        'total' : total ,
        'deaths' : deaths,
        'list' : list,
        'selectedcountry' : selectedcountry
        }
        return render(request , "home.html" , context)

    else:


        context = {'list' : list,}
        return render(request , "home.html",context)
