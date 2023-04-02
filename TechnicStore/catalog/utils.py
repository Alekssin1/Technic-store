from django.shortcuts import render
from django.contrib.auth import get_user_model

from users_page.forms import UserRegistrationForm, UserEmailLogin, UserPhoneLogin
from users_page.models import Bin


User = get_user_model()


class Notifications:
    errors = []
    temp_error = []
    success = []
    temp_success = []

    def add_to_temp(self, list_name, temp_name):
        temp_name.clear()
        temp_name = list_name.copy()
        list_name.clear()
        return temp_name


class CatalogMixin(Notifications):

    def renderPage(self):
        user_register = UserRegistrationForm()
        user_email_login = UserEmailLogin()
        user_phone_login = UserPhoneLogin()

        self.temp_error = self.add_to_temp(self.errors, self.temp_error)
        self.temp_success = self.add_to_temp(self.success, self.temp_success)
        
        bin =  self.request.session.get('basket')
        
        context = {
            'register_form': user_register,
            'email_login_form': user_email_login,
            'phone_login_form': user_phone_login,
            'errors': self.temp_error,
            'success': self.temp_success,
            'basket': bin,
        }

        return context