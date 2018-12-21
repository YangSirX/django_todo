from django.db import models

# Create your models here.
class content(models.Model):
    content_text = models.CharField(max_length=200)
    pub_time = models.DateTimeField('date published')
    finish_time =models.DateTimeField('date finished')
    status = models.CharField(max_length=20)
    # def __str__(self):
    #     return self.content_text


