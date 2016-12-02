from django.db import models

# Create your models here.


class Verbiage(models.Model):
    # text = models.CharField(null=True, blank=True, max_length=2000)
    text = models.TextField(null=True, blank=True, max_length=2000)
    name = models.CharField(max_length=30)

    def __unicode__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.name