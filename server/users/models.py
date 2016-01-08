from django.db import models
<<<<<<< HEAD

# Create your models here.
class User(models.Model):
    UserID = models.CharField(max_length = 100)
    Password = models.CharField(max_length = 100)
    UserGroup = models.IntegerField()
    Email = models.CharField(max_length = 100)
    Url = models.URLField()
=======
from django.contrib.auth.models import User
# Create your models here.
class Operator(models.Model):
    uesr=models.OneToOneField(User)
    privilege = models.IntegerField()

class Administrator(models.Model):
    uesr=models.OneToOneField(User)
    privilege = models.IntegerField()

class Researcher(models.Model):
    uesr=models.OneToOneField(User)
    privilege = models.IntegerField()

    def __unicode__(self):
        return self.username

>>>>>>> df42a9685f2820b7f7c8abab8a52fe9c1e590fbe
