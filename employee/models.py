from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name