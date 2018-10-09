from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()

    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + \
                self.name +'('+ str(self.age) + ')>'

class user(models.Model):
    user_id = models.CharField(max_length=30)
    user_pass = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
