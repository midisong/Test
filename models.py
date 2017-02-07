#!/user/bin/python
# _*_ coding:utf-8
from __future__ import unicode_literals

from django.db import models

from django.contrib import admin

# Create your models here

class Book(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class BookAdmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(Book)
