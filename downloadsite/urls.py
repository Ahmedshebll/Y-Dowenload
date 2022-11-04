from django.urls import path 
from . import views

# Create your urls here.

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.style, name='style'),
]