from rest_framework import serializers
from playlist.models import Notify
#from .models import User (alternativa)

class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Notify
        fields = '__all__' #quais campos da modelo serão utilizados [name]
