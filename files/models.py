from django.db import models

class File(models.Model):
    class Meta():
        verbose_name = 'File'
        verbose_name_plural = 'Files'
    
    file = models.FileField(upload_to='files')
    name = models.CharField(max_length=200)