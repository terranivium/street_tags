from django.urls import path 
from street_tag import views

app_name = 'street_tag'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_photo/', views.add_photo, name='add_photo'),
]