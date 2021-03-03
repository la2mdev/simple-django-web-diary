from django.urls import path
from . import views


app_name = 'entries'
urlpatterns = [
    path('', views.index, name='index'),
    path('new-entry/', views.new_entry, name='new_entry')
]
