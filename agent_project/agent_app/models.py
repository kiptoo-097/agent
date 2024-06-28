from django.db import models

# Create your models here.

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True, null=True)
    extraction = models.TextField(blank=True, null=True)
    thesis = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.file.name
