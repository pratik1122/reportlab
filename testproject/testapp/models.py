from django.db import models

# Create your models here.



class Report(models.Model):
    name = models.CharField(max_length=32,null = True , blank= True)
    phone  = models.IntegerField()
    address = models.CharField(max_length=32,null = True , blank= True)

    def __str__(self):
        return  self.name