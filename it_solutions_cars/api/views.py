from rest_framework import viewsets

from cars.models import Car, Comment
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import MethodNotAllowed

from .serializers import CarSerializer, CommentSerializer
from .permissions import AuthorOrReadOnly

class CarViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт для получения списка автомобилей, детали автомобиля, CRUD операций.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AuthorOrReadOnly,)
    http_method_names = ('get', 'post', 'put', 'delete')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт для доступа к комментариям
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)
    # Запрещаем все методы кроме POST и GET
    http_method_names = ['post', 'get']

    def perform_create(self, serializer):
        """
        Передача в сериалайзер данных об автомобиле и авторе комментария
        """
        car_id = self.kwargs.get('car_pk')
        car = get_object_or_404(Car, pk=car_id)
        serializer.save(car=car, author=self.request.user)
