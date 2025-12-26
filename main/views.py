from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# function based view
def hello_view(request):
    return HttpResponse("<h1>hello world</h1>")

# class based view
class HelloView(View):
    def get(self,request):
        return HttpResponse("<h1>man class based viewman!</h1>")
