from django.urls import path
from .views import CarIndexView, CarCreateView, CarDetailView, CarUpdateView, CommentCreateView, CarDeleteView

urlpatterns = [
    path('', CarIndexView.as_view(), name='index'),
    path('cars/new', CarCreateView.as_view(), name='create'),
    path('cars/<int:pk>', CarDetailView.as_view(), name='detail'),
    path('cars/<int:pk>/update', CarUpdateView.as_view(), name='update'),
    path('cars/<int:pk>/add_comment', CommentCreateView.as_view(), name='add_comment'),
    path('cars/<int:pk>/delete', CarDeleteView.as_view(), name='delete'),
]

app_name = 'cars'