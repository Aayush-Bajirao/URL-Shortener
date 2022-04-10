from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!!")

def home_page(request):

    context = {
        "submitted" : False         #dicticnory to append with index.html
    }

    if request.method == 'POST':    #request.method tells about post or get
       # print(request.POST)        #request.POST   gets data given by user incase of POST
        data = request.POST
        long_url = data['longurl']
        custom_name = data['custom_name']

        print(long_url)
        print(custom_name)
        context["submitted"] = True
        context["long_url"] = long_url
        context["short_url"] = request.build_absolute_uri() + custom_name
            
    else:
        print("User is not sending anything")

    return render(request, "index.html", context)

def task_page(request):

    context = {
        "my_name" : "Aayush",       #dicticnory to append with index.html 
        "x" : 15
    }

    return render(request, "task.html", context)