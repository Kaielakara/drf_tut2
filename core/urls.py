from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("api", views.api_message, name='api_m'),
    path("api/model", views.api_model, name='model'),
    path("api/drf_intro", views.drf_model, name='drf_model')
]