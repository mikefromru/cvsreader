import json
from django.db import models

# Create your models here.

class Client(models.Model):

    username = models.CharField(max_length=255, blank=True, null=True)
    spent_money = models.PositiveSmallIntegerField(blank=True, null=True)
    gems = models.JSONField(blank=True, null=True)

    # @property
    # def gemslist(self):
        # return list(self.gems.all())

    # def set_gems(self, lst):
    #     self.gems = json.dumps(lst)

    # def get_gems(self):
    #     return json.loads(self.gems)

    def __str__(self):
        return self.username