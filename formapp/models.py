from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth.models import User


class Amarform(models.Model):
    user_info = JSONField()
    mobile_number = models.CharField(max_length = 20)
    professional_info = JSONField()