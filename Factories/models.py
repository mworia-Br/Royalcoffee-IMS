from django.db import models

# Create your models here.
class Growerscoop(models.Model):
    cooperative=models.CharField(max_length=256)
    county=models.CharField(max_length=256)
    location=models.CharField(max_length=256)
    address=models.CharField(max_length=256)
    total_factories=models.IntegerField(10)

    def __str__(self):
        return self.cooperative

class Factory(models.Model):
    factory_name=models.CharField(max_length=256)
    cooperative=models.CharField(max_length=256)
    region=models.CharField(max_length=256)
    variety=models.CharField(max_length=256)
    altitude=models.CharField(max_length=256)
    soil=models.CharField(max_length=256)
    process=models.CharField(max_length=256)
    total_members=models.IntegerField(max_length=10)

    def __str__(self):
        return self.factory_name

from django.contrib import admin
admin.site.register(Growerscoop)
admin.site.register(Factory)
