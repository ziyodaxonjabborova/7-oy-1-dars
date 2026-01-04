from django.urls import path
from . import views 

urlpatterns=[
   path("api/books/",views.BookListCreateApi.as_view(),name="books-list"),
   path("api/books/<int:pk>/",views.BookDetailApi.as_view(),name="book-detail"),
   path("api/hello/",views.HelloApi.as_view(),name="hello"),
   path("api/greet/",views.GreetApi.as_view(),name="greet"),
   path("api/echo/",views.EchoApi.as_view(),name="echo"),
   path("api/check-age/",views.AgeCheckApi.as_view(),name="checkage"),
   path("api/register/",views.RegisterApi.as_view(),name="register"),
   path("api/square/<int:n>/",views.SquareApi.as_view(),name="square"),
   
   
   
   
   
   
   
   
   
   
   
]