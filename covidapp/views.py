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


url1 = "https://api.covid19india.org/data.json"
response1 = requests.get(url1).json()


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
        for i in range(0,noofresults):
            if ("Afghanistan" == response['response'][i]['country'] ):
                new = response['response'][i]['cases']['new']
                active = response['response'][i]['cases']['active']
                critical = response['response'][i]['cases']['critical']
                recovered = response['response'][i]['cases']['recovered']
                total = response['response'][i]['cases']['total']
                deaths = int(total)-int(active)-int(recovered)




        context = {'list' : list,'new' : new ,
        'active':active,
        'critical' : critical,
        'recovered' : recovered ,
        'total' : total ,
        'deaths' : deaths,
        'list' : list,
        'selectedcountry' : "Afghanistan"}
        return render(request , "home.html",context)



def india(request):
    no = len(response1["statewise"])
    list1 = []
    for i in range(0,no):
        list1.append(response1["statewise"][i]["state"])

    if request.method == "POST":
        selectedstate = request.POST["selectedstate"]
        for i in range(0,no):
            if (selectedstate == response1['statewise'][i]['state'] ):
                    new = (response1['statewise'][i]['deltaconfirmed'])
                    active = int(response1['statewise'][i]['active'])
                    lastupdatedtime = response1['statewise'][i]['lastupdatedtime']
                    recovered = int(response1['statewise'][i]['recovered'])
                    total = response1['statewise'][i]['confirmed']
                    deaths = response1['statewise'][i]['deaths']
                    context = {
                    'new' : new ,
                    'active':active,
                    'lastupdatedtime' : lastupdatedtime,
                    'recovered' : recovered ,
                    'total' : total ,
                    'deaths' : deaths,
                    'list' : list1,
                    'selectedstate' : selectedstate,
                    }
                    return render(request , "india.html" , context)


    else:
        for i in range(0,no):
            if ("Total" == response1['statewise'][i]['state'] ):
                new = (response1['statewise'][i]['deltaconfirmed'])
                active = int(response1['statewise'][i]['active'])
                lastupdatedtime = response1['statewise'][i]['lastupdatedtime']
                recovered = int(response1['statewise'][i]['recovered'])
                total = response1['statewise'][i]['confirmed']
                deaths = response1['statewise'][i]['deaths']
                context = {'list' : list,'new' : new ,
                'active':active,
                'lastupdatedtime' : lastupdatedtime,
                'recovered' : recovered ,
                'total' : total ,
                'deaths' : deaths,
                'list' : list1,
                'selectedstate' : "Total"}

    return render(request , "india.html" , context)
