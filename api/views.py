from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MinerSerializer
from .models import Miner
from rest_framework.response import Response

class MinerView(generics.ListCreateAPIView):
    serializer_class = MinerSerializer
    queryset = Miner.objects.all()