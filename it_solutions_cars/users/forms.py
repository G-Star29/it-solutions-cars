from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class SignUpUserForm(UserCreationForm):
    """Форма для View, согласно которой принимаются входные данные"""
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username')