from django.shortcuts import render
import requests
def get_geographic_info(request):
    ip = request.META.get('REMOTE_ADDR')
    print(ip)
    # url='http://api.ipstack.com/'+str(ip)+'?access_key=3dc63ae05b2288d3bdb6ceaf97f18505'
    url='http://api.ipstack.com/183.82.219.127?access_key=3dc63ae05b2288d3bdb6ceaf97f18505'
    response=requests.get(url)
    data=response.json()
    return render(request,'testapp/info.html',data)
