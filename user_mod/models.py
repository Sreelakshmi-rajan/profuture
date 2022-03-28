from django.db import models
from django.contrib.auth.models import User

class userprofile(models.Model):
    userprofileid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    usertype=models.CharField(max_length=20)
