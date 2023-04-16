from django.urls import path

from items import views

urlpatterns = [
    path('items/', views.ItemsListAPIView.as_view(), name='items-list'),
    path('items/create/', views.ItemsCreateAPIView.as_view(), name='items-create'),
]