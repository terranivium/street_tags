from django.shortcuts import render
from street_tag.models import Photo
from django.http import HttpResponse 

def index(request):
	mapbox_access_token = 'pk.eyJ1IjoidGVycmFuaXZpdW0iLCJhIjoiY2tndGwxMmk3MGY1bTJ5bmFud3l4d2d2eSJ9.YaCL14cu5Hfc1dIXZcTN_A'
	photo_list = Photo.objects.order_by()[:5] #order by?

	context_dict = {}
	context_dict['photos'] = photo_list
	context_dict['mapbox_access_token'] = mapbox_access_token

	return render(request, 'street_tag/index.html', context=context_dict)
