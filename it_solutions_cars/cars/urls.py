from django.urls import path
from .views import CarIndexView, CarCreateView, CarDetailView, CarUpdateView

urlpatterns = [
    path('', CarIndexView.as_view(), name='index'),
    path('cars/new', CarCreateView.as_view(), name='create'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='detail'),
    path('cars/<int:pk>/update', CarUpdateView.as_view(), name='update'),
]

app_name = 'cars'