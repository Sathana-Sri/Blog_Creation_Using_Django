from django.db import models

# Create your models here.
#blogcreation
class BlogPost(models.Model):#Model default to create model(class)
    title=models.CharField(max_length=200)
    content=models.TextField()
    image=models.ImageField(upload_to='images/',blank=True)#empty field will be saved
    video=models.FileField(upload_to='videos/',blank=True)#file filed like excel,videos
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
