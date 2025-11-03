from rest_framework import serializers
from .models import WebsiteContent

class WebsiteContentSerializer(serializers.ModelSerializer):
    publication_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    
    class Meta:
        model = WebsiteContent
        fields = '__all__'