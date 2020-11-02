from django import forms 
from street_tag.models import Photo

class PhotoForm(forms.ModelForm):
	lon = forms.DecimalField(max_digits=9, decimal_places=6, help_text="Please enter the longitude.")
	lat = forms.DecimalField(max_digits=9, decimal_places=6, help_text="Please enter the latitude.")
	image = forms.ImageField(help_text="Please enter image.", required = True)

	# An inline class to provide
	class Meta:
		# Provide an association 
		model = Photo
		fields = ('lon', 'lat', 'image')