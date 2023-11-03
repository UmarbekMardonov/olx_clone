from datetime import datetime
from django.db import models
from django.db.models.functions import Coalesce
from django.contrib.gis.db import models


class CategoryManager(models.Manager):
    def with_count(self):
        return super().get_queryset().annotate(counts=models.Count("ads"))


class CategoryLittle(models.Model):
    title = models.CharField(max_length=220)
    objects = CategoryManager()


class SavdoTuri(models.Choices):
    money = 'pulga'
    free = 'tegin'
    obmen = 'obmen'


class CategoryBig(models.Model):
    title = models.CharField(max_length=220)
    categoryLittle = models.ForeignKey(CategoryLittle, on_delete=models.CASCADE)
    savdo_turi = models.CharField(max_length=20, choices=SavdoTuri, default=SavdoTuri.money)


class Adds(models.Model):
    title = models.ForeignKey(CategoryLittle, on_delete=models.CASCADE, related_name='ads')
    image = models.ImageField(upload_to='media')
    location = models.PointField()
    phone_number = models.IntegerField()
    email = models.EmailField()
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)


'''
class Region(models.Model):
    title = models.CharField(max_length=220)


class District(models.Model):
    title = models.CharField(max_length=220)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class School(models.Model):
    title = models.CharField(max_length=220)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    pupil = models.ForeignKey(Pupil, related_name='school')


class Pupil(models.Model):
    name = models.CharField(max_length=220)
    ball = models.IntegerField()
'''
