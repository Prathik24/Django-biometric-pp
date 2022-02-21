from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from  .forms import *


# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World")


def myfunctionabout(request):
    return HttpResponse("About Response")


def add(request, a, b):
    return HttpResponse(a + b)


def intro(request, name, age):
    mydictionary = {
        "name": name,
        "age": age
    }
    return JsonResponse(mydictionary)


def mult(request, c, d):
    return HttpResponse(c * d)


def myfirstpage(request):
    return render(request, 'index.html')


def mysecondpage(request):
    return render(request, 'second.html')


def mythirdpage(request, mydictionary=None):
    var = "Hello world"
    greetings = "Hey how are you"
    fruits = ["apple", "mango", "pear"]
    num1, num2 = 20, 10
    ans = num1 > num2
    # print(ans)
    mydictionary = {
        "var": var,
        "msg": greetings,
        "myfruits": fruits,
        "ans": ans,
        "num1": num1,
        "num2": num2,

    }
    return render(request, 'third.html', context=mydictionary)


def myimagepage(request):
    return render(request, 'imagepage.html')


def myimagepage2(request):
    return render(request, 'imagepage2.html')


def myform(request):
    return render(request,'myform.html')


def submitmyform(request):
    mydictionary= {

         "var1": request.POST.get('mytext'),

         "var2": request.POST.get('mytextarea'),

        "method" :  request.method
    }
    return JsonResponse(mydictionary)



def myform2(request, mydictionary=None):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            mydictionary = {
                "form": FeedbackForm()

            }
            mydictionary["success"] = True
            mydictionary["successmsg"]= "Form Submitted"
            return render(request, 'myform2.html', context=mydictionary)


        elif request.method == "GET":
            form = FeedbackForm()
            mydictionary = {
                "form" : form
            }
            return render(request , 'myform2.html' , context=mydictionary)

















