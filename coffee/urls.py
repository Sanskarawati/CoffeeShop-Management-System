from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('home1',views.home1),
    path('contact',views.contact),
]