from django.urls import path

from . import views

urlpatterns = [
    path('', views.ItemListApiView.as_view(), name='list_create'),
    path('<int:pk>/update', views.ItemUpdateView.as_view(), name='item_view'),
    path('<int:pk>/delete', views.ItemDeleteView.as_view(), name='item_view'),
    path('<int:pk>', views.ItemRetrieveView.as_view(), name='item_view'),
]