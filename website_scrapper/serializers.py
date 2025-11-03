from rest_framework import serializers
from .models import Website_Content

class WebsiteContentSerializer(serializers.ModelSerializer):
    publication_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    
    class Meta:
        model = Website_Content
        fields = '__all__'