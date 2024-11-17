from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter


from .views import CarViewSet, CommentViewSet

router = DefaultRouter()

router.register(r'cars', CarViewSet)
router.register(r'cars/(?P<car_pk>\d+)/comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

app_name = 'api'