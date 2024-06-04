from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content= models.TextField()
    auth= models.ForeignKey( User, on_delete=models.CASCADE, default=1 )
    date_created= models.DateTimeField(auto_now_add=True)

    class meta:
        order_by = ('-date_created',)
 
def __str__(self):
    return self.title  