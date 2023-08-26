from django.db import models

# Create your models here.

class File(models.Model):

    file = models.FileField(upload_to='csv_files')

    def __str__(self) -> str:
        return str(self.file)

class Client(models.Model):

    username = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.username
    # total = models.Po
    # date = 
    # spent_money = models.CharField(max_length=50)
