from django.db import models

# Create your models here.
class Animal(models.Model):
    animalID = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    sound = models.CharField(max_length=10)

    def __str__(self):
        return self.animalID + " " + self.type + " " + self.sound

class Dog(Animal):
    name = models.CharField(max_length=10,null=False)
    age = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.age + " " + self.type

