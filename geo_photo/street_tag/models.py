from django.db import models

class Photo(models.Model):
	lon = models.DecimalField(max_digits=9, decimal_places=6)
	lat = models.DecimalField(max_digits=9, decimal_places=6)
	image = models.ImageField(blank=True)
