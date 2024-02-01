from django.db import models 

#Create your models here  
class Receipe(models.Model):
  reciepe_name=models.CharField(max_length=50)
  reciepe_desc=models.TextField()
  reciepe_image=models.ImageField(upload_to="reciepies")