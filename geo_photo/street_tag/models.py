from django.db import models
from django.core.exceptions import ValidationError

# image upload validation
def validate_image(image):
	max_height = 350
	max_width = 350
	height = image.height
	width = image.width
	if width > max_width or height > max_height:
		raise ValidationError("Height or Width is larger than what is allowed (350px)")

class Photo(models.Model):
	lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	image = models.ImageField(blank=True, null=True, validators=[validate_image])
