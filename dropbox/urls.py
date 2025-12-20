from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = 'dropbox'

urlpatterns = [
    path('', views.ContentListView.as_view(), name='listview'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('create/', views.ContentCreateView.as_view(), name='listcreate'),
    path('<int:pk>/', views.DetailView.as_view(), name='detailview'),
]