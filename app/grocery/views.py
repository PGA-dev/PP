from django.shortcuts import render
from typing import overload
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from grocery.models import Grocery

# Create your views here.

class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'grocery/index.html'


    def get(self, request):
        queryset = Grocery.objects.all()
        return Response({'grocery': queryset})
