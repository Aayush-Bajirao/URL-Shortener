from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!!")

def home_page(request):
    
    if request.method == 'POST':    #request.method tells about post or get
       # print(request.POST)         #request.POST   gets data given by user incase of POST
        data = request.POST
        long_url = data['longurl']
        custom_name = data['custom_name']

        print(long_url)
        print(custom_name)

    else:
        print("User is not sending anything")

    return render(request, "index.html")