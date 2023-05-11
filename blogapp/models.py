from django.db import models

# Create your models here.
class Blog(models.Model):

    
    
    name=models.CharField(max_length=100)
    caste=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()
    author=models.CharField(max_length=90)
    date=models.DateField()
    comment=models.TextField(default="hai")
    

    def __str__(self):
        return self.name
