from django.db import models

class Photo(models.Model):
	lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	image = models.ImageField(blank=True, null=True)
