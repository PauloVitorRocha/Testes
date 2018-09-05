from django.shortcuts import render
from rest_framework import viewsets
from playlist.models import Notify
from playlist.serializers import NotifySerializer

class NotifyViewSet(viewsets.ModelViewSet):
    queryset = Notify.objects.all()
    serializer_class = NotifySerializer
