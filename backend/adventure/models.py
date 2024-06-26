from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    targets = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name