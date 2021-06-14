from django.db import models

class Comment(models.Model):
    email=models.EmailField(primary_key=True,max_length=30)
    c_date=models.DateField(auto_now_add=True)
    comment=models.TextField()
