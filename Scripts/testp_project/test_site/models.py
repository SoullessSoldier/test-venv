from django.db import models

# Create your models here.
class test_model(models.Model):
    fio=models.CharField(max_length=100)
    firma=models.CharField(max_length=100)
    email=models.EmailField()
    export_to_pdf=models.DateTimeField(null=True)
    sent_email=models.DateTimeField(null=True)
    
    def __str__(self):
        return self.fio