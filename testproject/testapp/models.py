from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from django.http import HttpResponse
from testapp.utils import render_to_pdf


class Report(models.Model):
    name = models.CharField(max_length=32,null = True , blank= True)
    phone  = models.IntegerField()
    address = models.CharField(max_length=32,null = True , blank= True)

    def __str__(self):
        return  self.name




@receiver(post_save,sender = Report)
def create_pdf(sender,instance,**kwargs):
    report = Report.objects.all()

    pdf = render_to_pdf('pdf/details.html', {'report': report})
    return HttpResponse(pdf, content_type='application/pdf')




