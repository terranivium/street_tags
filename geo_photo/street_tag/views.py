from django.shortcuts import render

from django.http import HttpResponse 

def index(request):
	mapbox_access_token = 'pk.eyJ1IjoidGVycmFuaXZpdW0iLCJhIjoiY2tndGwxMmk3MGY1bTJ5bmFud3l4d2d2eSJ9.YaCL14cu5Hfc1dIXZcTN_A'
	return render(request, 'street_tag/index.html', { 'mapbox_access_token':mapbox_access_token })
