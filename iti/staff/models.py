from django.db import models
from courses.models import Courses

# Create your models here.
class Staff(models.Model):
    name=models.CharField(max_length=30)
    salary=models.TextField(null=True)
    age=models.TextField(null=True)
    courses= models.ManyToManyField(Courses)
    def __str__(self):
        return self.name

