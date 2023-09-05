import json
from django.db import models


class Client(models.Model):

    username = models.CharField(max_length=255, blank=True, null=True)
    spent_money = models.PositiveBigIntegerField(blank=True, null=True)
    gems = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.username