from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from django.shortcuts import get_object_or_404


# ======================================================
# 1-TOPSHIRIQ
# ======================================================
class BookListCreateApi(APIView):
    
    def get(self,request):
        objs=Book.objects.all()
        books=[]
        for book in objs:
            books.append(
                {
                    "id":book.pk,
                    "title":book.title,
                    "author":book.author,
                    "year":book.year,
                    "price":book.price
                }
            )
        return Response(data=books)
    
    def post(self,request):
        data=request.data
        obj=Book.objects.create(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            price=data["price"], 
        )
        book={"id":obj.pk,
              "title":obj.title,
              "author":obj.author,
              "year":obj.year,
              "price":obj.price
              }
        return Response(data=book,status=201)
    
class BookDetailApi(APIView):
    
    def get(self,request,pk):
        obj=get_object_or_404(Book,pk=pk)
        book={"id":obj.pk,
              "title":obj.title,
              "author":obj.author,
              "year":obj.year,
              "price":obj.price
              }
        return Response(data=book)
    
    def put(self,request,pk):
        obj=get_object_or_404(Book,pk=pk)
        book=request.data
        obj.title=book["title"]
        obj.author=book["author"]
        obj.year=book["year"]
        obj.price=book["price"]
        obj.save()
        book={"id":obj.pk,
              "title":obj.title,
              "author":obj.author,
              "year":obj.year,
              "price":obj.price
              }
        return Response(data=book)
    
    def patch(self,request,pk):
        obj=get_object_or_404(Book,pk=pk)
        book=request.data
        obj.title=book.get("title",obj.title)
        obj.author=book.get("author",obj.author)
        obj.year=book.get("year",obj.year)
        obj.price=book.get("price",obj.price)
        obj.save()
        book={"id":obj.pk,
              "title":obj.title,
              "author":obj.author,
              "year":obj.year,
              "price":obj.price
              }
        return Response(data=book)
    
    def delete(self,request,pk):
        obj=get_object_or_404(Book,pk=pk)
        obj.delete()
        return Response(status=204)
    
# ======================================================
# 2-TOPSHIRIQ
# ======================================================

# 1-API:

class HelloApi(APIView):
    def get(self,request):
        return Response(data={"message":"Hello API!"})
    
# 2-API:

class GreetApi(APIView):
    def get(self,request):
        name=request.query_params.get("name")
        return Response(data={"message":f"Hello {name} !!"})
    
# 3-API:
class EchoApi(APIView):
    def post(self,request):
        matn=request.data.get("text")
        return Response(data={"matn":f"{matn}"})
    
# 4-API:

class AgeCheckApi(APIView):
    def post(self,request):
        age=request.data.get("age")
        if age<18:
            return Response(data={"message":"Access denied 🚫"})
        else:
            return Response(data={"message":"Access granted ✅"})
        
# 5-API:

class RegisterApi(APIView):
    def post(self,request):
        data=request.data
        if not data.get("username"):
            return Response(status=400)
        else:
            return Response(data={"message":"User registered ✅"},status=201)
        
        
# 6-API:
class SquareApi(APIView):
    def get(self,request,n):
        sq=n**2
        return Response(data={
            "number":n,
            "square":sq
        })
        

        
        

            
            
            
            
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
