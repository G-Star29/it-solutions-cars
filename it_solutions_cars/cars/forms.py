from datetime import datetime

from django import forms
from .models import Car, Comment


class CarCreationForm(forms.ModelForm):
    """
    Форма для создания записи об автомобиле
    """
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'description')

    year = forms.IntegerField(
        widget=forms.NumberInput(),
        min_value=1885,
        max_value=datetime.utcnow().year,
    )

    def save(self, commit=True, user=None):
        """
        Добавляет данные о владельце записи в форму
        """
        car = super().save(commit=False)
        if user:
            car.owner = user
        if commit:
            car.save()

        return car

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)