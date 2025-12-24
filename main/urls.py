from django.urls import path
from .views import *


urlpatterns=[
    path("api/books/",BookListApi.as_view(),name="all_books"),
    path("api/hello/", HelloApi.as_view(), name="hello"),
    path("api/greet/", GreetApi.as_view(), name="greet"),
    path("api/echo/", EchoApi.as_view(), name="echo"),
    path("api/check-age/", CheckAgeApi.as_view(), name="check-age"),
    path("api/register/", RegisterApi.as_view(), name="register"),
    path("api/square/<int:number>/", SquareApi.as_view(), name="square"),

    
]