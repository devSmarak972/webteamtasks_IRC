from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from distutils.command.upload import upload
from django.db import models

# Create your models here.
from datetime import date
import uuid

import json


class University(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    Info = models.TextField(blank=True, null=True)
    Address = models.TextField(blank=True, null=True)
    Email = models.EmailField(
        _('email address'), blank=True, null=True)
    Website = models.TextField(blank=True, null=True)
    Expense = models.TextField(blank=True, null=True)
    Country = models.CharField(max_length=100, blank=True, null=True)
    Deadline = models.DateField(blank=True, null=True)
    Continent = models.CharField(max_length=100, blank=True, null=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(
        upload_to="images/university/", default='/images/university/university2.jpg', blank=True, null=True)

    def __str__(self):
        return self.Name


class Profile(AbstractBaseUser, PermissionsMixin):
    Username = models.CharField(
        max_length=200, blank=True, null=True, unique=True)
    Email = models.EmailField(
        _('email address'), unique=True, blank=True, null=True)
    Bookmarks = models.TextField(
        blank=True, null=True, default='{"bookmarks":[]}')
    Applications = models.TextField(
        blank=True, null=True, default='{"applications":[]}')
    profileimg = models.ImageField(
        upload_to="images/users", default='/images/users/profile.png', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = []
    # REQUIRED_FIELDS = ['Email']
    USERNAME_FIELD = 'Username'
    objects = CustomUserManager()

    def getBookmarks(self):
        return json.loads(self.Bookmarks)

    def setBookmarks(self, x):
        print("in model")
        print(json.dumps(x))
        self.Bookmarks = json.dumps(x)
        self.save()

    def getApplications(self):
        return json.loads(self.Applications)

    def setApplications(self, x):
        self.Applications = json.dumps(x)
        self.save()

    def __str__(self):
        return self.Username


class Notifications(models.Model):
    headline = models.CharField(max_length=255, blank=True, null=True)
    body_text = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    user = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.headline
