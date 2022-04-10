from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import LongToShort



def hello_world(request):
    return HttpResponse("Hello World!!")

def home_page(request):

    context = {
        "submitted" : False,         #dicticnory to append with index.html
        "error" : False,
    }

    if request.method == 'POST':    #request.method tells about post or get
        context["submitted"] = True

       # print(request.POST)        #request.POST   gets data given by user incase of POST
        data = request.POST
        long_url = data['longurl']
        custom_name = data['custom_name']

        try:
            obj = LongToShort(long_url = long_url, short_url = custom_name)        
            obj.save()                  #Actually adding database to SQL through django

            context["date"] = obj.date  #Date for link
            context["clicks"] = obj.clicks
            context["long_url"] = long_url
            context["short_url"] = request.build_absolute_uri() + custom_name
        except:
            context["error"] = True
        
        
    return render(request, "index.html", context)


def redirect_url(request, short_url):
    row = LongToShort.objects.filter(short_url = short_url)     #Filter for fetching row from database
    if len(row) == 0:                                           #Error handling
        return HttpResponse("No reponse")
    obj = row[0]
    long_url = obj.long_url                                  #Accessing required column 
    obj.clicks = obj.clicks + 1   
    obj.save()                        #row[1]==obj
    return redirect(long_url)                                   #Redirecting the link 


def task_page(request):

    context = {
        "my_name" : "Aayush",       #dicticnory to append with index.html 
        "x" : 15
    }

    return render(request, "task.html", context)
