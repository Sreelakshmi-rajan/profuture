from argparse import ONE_OR_MORE
from django.db import models
from django.contrib.auth.models import User

class userprofile(models.Model):
    userprofileid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    usertype=models.CharField(max_length=20)

class userdetails(models.Model):
    detailid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.CharField(max_length=10)
    companyinstitution=models.CharField(max_length=30,default="")

class clientproject(models.Model):
    projectid=models.AutoField(primary_key=True)
    detailid=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    projectname=models.CharField(max_length=30)




