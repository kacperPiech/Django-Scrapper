from rest_framework import viewsets
from .models import Website_Content
from .serializers import WebsiteContentSerializer

class WebsiteContentViewSet(viewsets.ModelViewSet):
    serializer_class = WebsiteContentSerializer
    
    def get_queryset(self):
        queryset = Website_Content.objects.all().order_by('-publication_date')
        source = self.request.query_params.get('source')
        if source:
            queryset = queryset.filter(url__icontains=source)
        return queryset

