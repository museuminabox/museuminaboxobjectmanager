from django.db import models


class Organisation(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name
