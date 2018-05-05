from django.db import models

class Task(models.Model):
    pic_name = models.CharField(max_length=20)
    pic_desc = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg')

    def __str__(self):
        return self.pic_name
