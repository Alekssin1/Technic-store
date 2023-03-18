from django import forms

from .models import User


class UserRegistrationForm(forms.ModelForm):
    """Form class for creation user"""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'email', 'password')
        labels = {'first_name': '', 'last_name': '',
                  'phone': '', 'email': '', 'password': '', }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'register__input', "placeholder": "Ім'я", "type": "text", }),
            'last_name': forms.TextInput(attrs={'class': 'register__input', "placeholder": "Прізвище", "type": "text", }),
            'phone': forms.TextInput(attrs={'class': 'register__input', "placeholder": "Номер телефону", "type": "text", }),
            'email': forms.TextInput(attrs={'class': 'register__input', "placeholder": "Email", "type": "email", }),
            'password': forms.TextInput(attrs={'class': 'register__input', "placeholder": "Пароль", "type": "password", }),
        }


class UserEmailLogin(forms.Form):
    
    email = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'login__input login__email', "placeholder": "Email", "type": "email", }))
    password = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'login__input login__email', "placeholder": "Пароль", "type": "password"}))


class UserPhoneLogin(forms.Form):

    phone = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'login__input login__number', "placeholder": "Номер телефону", "type": "text", }))
    password = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'login__input login__number', "placeholder": "Пароль", "type": "password"}))