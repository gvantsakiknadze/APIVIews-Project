from django.shortcuts import render

from rest_framework.response import Response
from .models import Book
from . import serializers
from rest_framework.views import APIView


# Create your views here.
class SelectBookView(APIView):
    def get(self, request, pk= None):
        if pk:
            try:
                data=Book.objects.get(pk=pk)
                serializer = serializers.BookSerializers(data, context={"request": request}, many=False)
                return Response(serializer.data)
            except:
                return Response("Could not find a book")
        data = Book.objects.all().order_by('id')
        # requestidan datas aserializebs
        serializer = serializers.BookSerializers(data, context={"request": request}, many=True)
        return Response(serializer.data)


class AddBookView(APIView):
    def post(self, request):
        serializer = serializers.BookSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




class DeleteBookView(APIView):
    def delete(self,request,pk):
        event = Book.objects.get(pk=pk)
        event.delete()
        return Response("Deletion Successful!")

