from django.db import models
from datetime import datetime

class Movie(models.Model):
    movieid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    year=models.IntegerField()
    director=models.CharField(max_length=30)
    imgurl=models.TextField()
    rentalprice = models.DecimalField(default=0.00,decimal_places=2,max_digits=12)
    active=models.BooleanField(default=True)

class User(models.Model):
    userid=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=40)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    type=models.IntegerField(default=2)# 1-Admin 2-Client
    active=models.BooleanField(default=True)


class Rent(models.Model):
     rentid=models.AutoField(primary_key=True)
     user = models.ForeignKey(User,on_delete=models.CASCADE,)
     renteddate = models.DateTimeField(default=datetime.now)
     totalamount = models.DecimalField(default=0.00,decimal_places=2,max_digits=12)
     haspenalty=models.BooleanField(default=False)
     delivereddate = models.DateTimeField(null=True, blank=True)
     inprocess=models.BooleanField(default=True)
     active=models.BooleanField(default=True)


class RentMovies(models.Model):
    rentmoviesid=models.AutoField(primary_key=True)
    rent = models.ForeignKey(Rent,on_delete=models.CASCADE,)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,)
    
