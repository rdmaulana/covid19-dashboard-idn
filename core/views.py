import requests, json, datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from datetime import date, timedelta
from .models import covidRecord

today = date.today()
start = date(2020, 3, 22)
end = today

url = "https://covid-193.p.rapidapi.com/statistics"
url_history = "https://covid-193.p.rapidapi.com/history"

headers = {
    'x-rapidapi-key': settings.API_KEY,
    'x-rapidapi-host': settings.API_HOST  
}

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def dashboard(request):
    querystring = {"country":"indonesia"}
    response = requests.request("GET", url, headers=headers, params=querystring).json()

    total = response['response'][0]['cases']['total']
    new_cases = response['response'][0]['cases']['new']
    active_cases = response['response'][0]['cases']['active']
    recovered_cases = response['response'][0]['cases']['recovered']

    deaths = response['response'][0]['deaths']['total']
    new_deaths = response['response'][0]['deaths']['new']

    total_populations = response['response'][0]['population']
    total_tests = response['response'][0]['tests']['total']

    #cases chart line code
    
    chart_new_cases = []
    chart_recovered_cases = []
    chart_death_cases = []

    chart_1m_cases = []
    chart_1m_deaths = []
    chart_1m_tests = []

    start_date =  today - timedelta(days=7)
    end_date = today

    dates = [date for date in daterange(start_date, end_date)]
    datatables = []

    # for date in daterange(start_date, end_date):
    #     dates.append(str(date))

    for date in dates:
        querystring = {"country":"indonesia","day":date}
        crawl = requests.request("GET", url_history, headers=headers, params=querystring).json()
        datatables.append(crawl)

        chart_new_cases.append(int(crawl['response'][0]['cases']['new']))
        chart_recovered_cases.append(int(crawl['response'][0]['cases']['recovered']))
        chart_death_cases.append(int(crawl['response'][0]['deaths']['new']))

        chart_1m_cases.append(int(crawl['response'][0]['cases']['1M_pop']))
        chart_1m_deaths.append(int(crawl['response'][0]['deaths']['1M_pop']))
        chart_1m_tests.append(int(crawl['response'][0]['tests']['1M_pop']))

    #end cases chart line code

    context = {
        'response':datatables,
        'total':total, 
        'new_cases':new_cases,
        'active_cases':active_cases,
        'recovered_cases':recovered_cases,
        'deaths':deaths,
        'new_deaths':new_deaths,
        'chart_new_case': chart_new_cases,
        'chart_recovered_cases': chart_recovered_cases,
        'chart_death_cases': chart_death_cases,
        'chart_date_range': dates,

        'chart_1m_cases' : chart_1m_cases,
        'chart_1m_deaths' : chart_1m_deaths,
        'chart_1m_tests' : chart_1m_tests,

        'total_populations': total_populations,
        'total_tests': total_tests
    }

    return render(request, 'app/dashboard.html', context=context)


