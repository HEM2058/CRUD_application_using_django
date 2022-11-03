from django.db import models

# Create your models here.
class Teacher(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.BigIntegerField()
#  this function is used for converting object into string
    def __str__(self) -> str:
        return self.Firstname