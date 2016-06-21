from django.db import models
from django.utils import timezone

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    score = models.FloatField(default=0.0)
    member_1 = models.CharField(max_length=100)
    member_2 = models.CharField(max_length=100, blank=True)
    member_3 = models.CharField(max_length=100, blank=True)
    member_4 = models.CharField(max_length=100, blank=True)
    email_1 = models.EmailField()
    email_2 = models.EmailField(blank=True)
    email_3 = models.EmailField(blank=True)
    email_4 = models.EmailField(blank=True)
    SHIRT_SIZES = (
        ('', 'None'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        )
    size_1 = models.CharField(max_length=1, choices=SHIRT_SIZES, default='', null=True, blank=True)
    size_2 = models.CharField(max_length=1, choices=SHIRT_SIZES, default='', null=True, blank=True)
    size_3 = models.CharField(max_length=1, choices=SHIRT_SIZES, default='', null=True, blank=True)
    size_4 = models.CharField(max_length=1, choices=SHIRT_SIZES, default='', null=True, blank=True)
    diet = models.CharField(max_length=1000, blank=True)
    code = models.FileField(upload_to='uploads/', null=True, blank=True)
    last_login = models.DateTimeField(null=True)

    REQUIRED_FIELDS = ['password', 'member_1', 'email_1']
    USERNAME_FIELD = 'name'
