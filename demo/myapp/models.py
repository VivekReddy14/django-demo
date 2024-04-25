from django.db import models

# Create your models here.

class Catalog(models.Model):
    Name = models.CharField(max_length = 64)
    Class = models.CharField(max_length = 64)
    School = models.CharField(max_length = 64)
    State = models.CharField(max_length = 64)
    created = models.DateTimeField(auto_now_add = True)