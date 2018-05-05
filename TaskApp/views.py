from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Task
from . Serializers import TaskSerializer
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializer


class DueTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSerializer


class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = TaskSerializer
