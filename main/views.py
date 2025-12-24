from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book

class BookListApi(APIView):
    def get(self,request):
        books=Book.objects.all()
        kitoblar=[]
        for book in books:
            kitoblar.append(
                {
                    "id":book.id,
                    "title":book.title,
                    "author":book.author,
                    "published_year":book.published_year,
                    "price":book.price,
                }
            )
        
        return Response(data=kitoblar,status=200)
    
    def post(self,request):
        data=request.data
        book=Book.objects.create(
            title=data['title'],
            author=data['author'],
            published_year=data['published_year'],
            price=data['price']
        )
        json_book={
                    "id":book.id,
                    "title":book.title,
                    "author":book.author,
                    "published_year":book.published_year,
                    "price":book.price,
                }
        
        return Response(data=json_book,status=201)
    
# DETAIL,DELETE,UPDATE

# 1-api: Hello API
class HelloApi(APIView):
    def get(self, request):
        return Response({"message": "Hello, API!"})


# 2-api: Greet API
class GreetApi(APIView):
    def get(self, request):
        name = request.query_params.get("name", "Guest") 
        return Response({"message": f"Hello, {name}"})


# 3-api: Echo API
class EchoApi(APIView):
    def post(self, request):
        text = request.data.get("text")
        return Response({"matn": text})


# 4-api: Check age API
class CheckAgeApi(APIView):
    def post(self, request):
        age = request.data.get("age")
        if age is None:
            return Response({"error": "Age not provided"}, status=400)
        try:
            age = int(age)
        except ValueError:
            return Response({"error": "Invalid age"}, status=400)

        if age < 18:
            return Response({"message": "Access denied"})
        return Response({"message": "Access granted"})


# 5-api: Register API
class RegisterApi(APIView):
    def post(self, request):
        username = request.data.get("username")
        if not username:
            return Response({"error": "Username required"}, status=400)
        return Response({"message": "User registered"}, status=201)


# 6-api: Square API
class SquareApi(APIView):
    def get(self, request, number):
        try:
            num = int(number)
        except ValueError:
            return Response({"error": "Invalid number"}, status=400)
        return Response({"number": num, "square": num**2})


        


