from django.db import models
from martor.models import MartorField


class Post(models.Model):
    text = MartorField()
