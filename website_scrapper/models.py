from django.db import models

class WebsiteContent(models.Model):
    title = models.CharField(max_length = 150)
    website_html_content = models.TextField()
    website_plain_content = models.TextField()
    url = models.URLField(unique = True)
    publication_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.title} at {self.publication_date}"
    
    

