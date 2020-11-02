from django import forms 
from street_tag.models import Photo

class PhotoForm(forms.ModelForm):
	lon = forms.DecimalField(max_digits=18, decimal_places=15, help_text="Longitude: ")
	lat = forms.DecimalField(max_digits=17, decimal_places=15, help_text="Latitude: ")
	image = forms.ImageField(help_text="Image: ", required = True)

	# An inline class to provide
	class Meta:
		# Provide an association 
		model = Photo
		fields = ('lon', 'lat', 'image')