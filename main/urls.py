from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete_runkeeper', views.complete_runkeeper, name='complete_runkeeper'),
]
