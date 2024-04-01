from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse

# Create your views here.
class TaskListCreate(APIView):
    def get(self,request,format=None):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
class TaskRetrieveUpdateDestroy(APIView):
    def get(self,request,pk,format=None):
        try:
            task=Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=TaskSerializer(task)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        try:
            task=Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

def add(request):
    return HttpResponse("<h1>Hello World </h1>")