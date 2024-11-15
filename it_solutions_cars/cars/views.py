from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

from .models import Car, Comment
from .forms import CarCreationForm, CommentForm


class CarIndexView(ListView):
    """ListView для отображения списка записей об автомобилях"""
    model = Car
    context_object_name = 'cars'



class CarCreateView(LoginRequiredMixin, CreateView):
    """CreateView для отображения формы для ввода данных об автомобилях (создать запись)"""
    model = Car
    form_class = CarCreationForm
    template_name = 'cars/car_create.html'
    success_url = reverse_lazy('cars:index')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):

        form.instance.owner = self.request.user

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
        context['comment_form'] = CommentForm()
        return context

class CarUpdateView(LoginRequiredMixin, UpdateView):
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


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'cars/car_detail.html'


    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            messages.error(self.request, "Только зарегистрированные пользователи могут оставлять комментарии.")
            return redirect('cars:detail', pk=self.kwargs['pk'])
        car = get_object_or_404(Car, pk=self.kwargs['pk'])
        form.instance.car = car
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('cars:detail', kwargs={'pk': self.object.pk})

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    context_object_name = 'car'
    success_url = reverse_lazy('cars:index')


    def dispatch(self, request, *args, **kwargs):
        if self.get_object().owner != self.request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)