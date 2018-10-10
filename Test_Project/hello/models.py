from django.db import models

class user(models.Model):
    user_id = models.CharField(max_length=16,primary_key=True)
    user_pass = models.CharField(max_length=20)
    email = models.EmailField(max_length=120)


class tweet(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<message:id=' + str(self.id) + ',' + self.title + '(' + str(self.pub_date) + ')>'

    class Meta:
        ordering = ('pub_date',)
