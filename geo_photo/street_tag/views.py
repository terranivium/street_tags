from django.shortcuts import render
from street_tag.models import Photo
from django.http import HttpResponse
from street_tag.forms import PhotoForm
from django.shortcuts import redirect

def index(request):
	mapbox_access_token = 'pk.eyJ1IjoidGVycmFuaXZpdW0iLCJhIjoiY2tndGwxMmk3MGY1bTJ5bmFud3l4d2d2eSJ9.YaCL14cu5Hfc1dIXZcTN_A'
	photo_list = Photo.objects.order_by()

	form = PhotoForm()

	# A HTTP POST?
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
	        
	    # Have we been provided with a valid form?
		if form.is_valid():
			# Save the new category to the database. 
			form.save(commit=True) 
			# For now, just redirect the user back to the index view. 
			return redirect('/')
		else:
			# just print them to the terminal.
			print(form.errors)

	context_dict = {}
	context_dict['photos'] = photo_list
	context_dict['mapbox_access_token'] = mapbox_access_token
	context_dict['form'] = form

	return render(request, 'street_tag/index.html', context=context_dict)
