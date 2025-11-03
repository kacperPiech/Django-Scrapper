from rest_framework import serializers
from .models import Website_Content

class WebsiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website_Content
        fields = '__all__'