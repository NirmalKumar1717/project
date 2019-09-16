from django.db import models

# Create your models here.
class table(models.Model):
   name = models.TextField(max_length=100)
   age = models.IntegerField()
   Qualification = models.TextField(max_length=100)
   year_of_passing = models.IntegerField()
   #img = models.Imagefiels(upload_to='filename')