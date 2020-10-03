from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

# class Creator(models.Model):
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     def get_fullname(self):
#         return self.created_by.get_username()


class Cuboid(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # creator = models.ManyToManyField(Creator, related_name='staff_product')
    title = models.CharField(max_length=80)
    length = models.ForeignKey('FilterLength', on_delete=models.CASCADE)
    width = models.ForeignKey('FilterWidth', on_delete=models.CASCADE)
    height = models.ForeignKey('FilterHeight', on_delete=models.CASCADE)
    area = models.ForeignKey('FilterArea', on_delete=models.CASCADE)
    volume = models.ForeignKey('FilterVolume', on_delete=models.CASCADE,)
    created_on= models.DateTimeField(default=datetime.now())
    last_updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_length(self):
        return self.length.length

    def get_width(self):
        return self.width.width

    def get_height(self):
        return self.height.height

    def get_area(self):
        return self.area.area

    def get_volume(self):
        return self.volume.volume



class FilterLength(models.Model):
    length = models.CharField(max_length=30)
    created_on = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.length

class FilterWidth(models.Model):
    width = models.CharField(max_length=30)
    created_on = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.width

class FilterHeight(models.Model):
    height = models.CharField(max_length=30)
    created_on = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.height

class FilterArea(models.Model):
    area = models.CharField(max_length=30)
    created_on = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.area

class FilterVolume(models.Model):
    volume = models.PositiveIntegerField()
    created_on = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.volume



