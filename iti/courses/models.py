from django.db import models

category_type=[
    ('9-Month','9-Month'),
    ('3-Month','3-Month'),
    ('1-Month','1-Month')
]
# Create your models here.
class Courses (models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=500)
    publish_at=models.DateTimeField(auto_now=True)
    last_modification=models.DateTimeField(auto_now_add=True)
    final_degree=models.IntegerField(default=100)
    category=models.CharField(max_length=15,choices=category_type) 
    photo=models.ImageField(upload_to='images')

    def __str__(self):
        return self.title