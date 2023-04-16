from django.urls import path, include

urlpatterns = [
    path('', include('resources.urls.v1')),
    path('', include('items.urls.v1')),
]
