from django.db import models

class Gemeinden(models.Model):
    land = models.IntegerField()
    gemeindekey = models.CharField(max_length=60)
    gemeinde = models.CharField(max_length=255)
    gewerbesteuer = models.IntegerField()

    def __str__(self):
        return self.gemeinde