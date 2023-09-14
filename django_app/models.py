from django.db import models

# Create your models here.
class reg_model(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    psw = models.CharField(max_length=20)
    def __str__(self):
        return self.first_name + self.last_name
class filemodel(models.Model):
    filename=models.CharField(max_length=30)
    file=models.FileField(upload_to="django_app/static")
    def __str__(self):
        return self.filename


class cardmodel(models.Model):
    product=models.CharField(max_length=30)
    price=models.IntegerField()
    discript=models.CharField(max_length=30)
    file=models.FileField(upload_to='django_app/static')

class videomodel(models.Model):
    videoname=models.CharField(max_length=30)
    video=models.FileField(upload_to='django_app/static')
    audioname = models.CharField(max_length=30)
    audio = models.FileField(upload_to='django_app/static')
    pdfname = models.CharField(max_length=30)
    pdf = models.FileField(upload_to='django_app/static')

class datemodel(models.Model):
    first_name= models.CharField(max_length=50)
    date = models.DateField()

class checkmodel(models.Model):

    choice=[
        ('kerala','kerala'),
        ('tamilnadu','tamilnadu'),
        ('karnataka','karnataka')


    ]
    firstname=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    date=models.DateField()
    state=models.CharField(max_length=20,choices=choice)
    eng=models.BooleanField()
    mal=models.BooleanField()
    hind=models.BooleanField()