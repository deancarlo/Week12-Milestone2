from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_hired = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
