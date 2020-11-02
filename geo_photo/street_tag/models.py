from django.db import models
from django.core.exceptions import ValidationError

# image upload validation
def validate_image(image):
	if image.size > 4*1024*1024:
		raise ValidationError("Filesize is too large (>4MB)")

class Photo(models.Model):
	lon = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
	lat = models.DecimalField(max_digits=17, decimal_places=15, blank=True, null=True)
	image = models.ImageField(blank=True, null=True, validators=[validate_image])
