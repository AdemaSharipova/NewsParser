from rest_framework.routers import DefaultRouter

from resources import views

router = DefaultRouter()
router.register(r'resources', views.ResourceViewSet)

urlpatterns = router.urls