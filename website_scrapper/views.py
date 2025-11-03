from rest_framework import viewsets
from .models import Website_Content
from .serializers import WebsiteContentSerializer

class WebsiteContentViewSet(viewsets.ModelViewSet):
    queryset = Website_Content.objects.all().order_by('-publication_date')
    serializer_class = WebsiteContentSerializer

