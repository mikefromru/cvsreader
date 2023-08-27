from django.db import models

# Create your models here.

class Client(models.Model):

    customer = models.CharField(max_length=255, blank=True, null=True)
    item = models.CharField(max_length=550, blank=True, null=True)
    total = models.PositiveSmallIntegerField(blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.customer