from rest_framework import serializers
from .models import QrcodeApi, TestModel



class ApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=QrcodeApi
        fields = ['title', 'date', 'qr_code']
        
        


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=TestModel
        fields = [ 'title', 'date', 'qr_code' ]
        
       
       
