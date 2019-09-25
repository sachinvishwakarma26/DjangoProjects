from django.shortcuts import render
import requests

def home(request):
    response = requests.get('http://api.ipstack.com/183.83.251.61?access_key=e3c7a54f1245040e4e044029ccaf8a89')
    data = response.json()
    dict={
        'ip': data['ip'],
        'country': data['country_name']
    }
    return render(request, 'testapp/info.html',dict )
