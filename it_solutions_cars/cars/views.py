from django.template.defaulttags import comment
from django.utils import timezone

from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy

from .models import Car, Comment
from .forms import CarCreationForm

class CarIndexView(ListView):
    """ListView для отображения списка записей об автомобилях"""
    model = Car
    context_object_name = 'cars'



class CarCreateView(CreateView):
    """CreateView для отображения формы для ввода данных об автомобилях (создать запись)"""
    model = Car
    form_class = CarCreationForm
    template_name = 'cars/car_create.html'
    success_url = reverse_lazy('cars:index')


    def form_valid(self, form):

        form.save(user=self.request.user)

        return super().form_valid(form)

class CarDetailView(DetailView):
    """DetailView для отображения записи с деталями"""
    model = Car
    context_object_name = 'car'
    template_name = 'cars/car_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.owner == self.request.user
        context['comments'] = self.object.comments.all()
        return context

class CarUpdateView(UpdateView):
    """UpdateView создает форму для редактирования записи ее владельцем"""
    model = Car
    form_class = CarCreationForm
    template_name = 'cars/car_create.html'

    def get_success_url(self):
        return reverse_lazy('cars:detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        """
        Переопределение функции dispatch

        Проверка на владельца записи
        """
        if self.get_object().owner != self.request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Добавляем текущее время в форму при редактировании записи
        """
        form.instance.updated_at = timezone.now()
        return super().form_valid(form)


