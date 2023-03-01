import base64
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import redirect

from catalog.utils import CatalogMixin, Notifications
from .forms import UserRegistrationForm, UserEmailLogin, UserPhoneLogin
from catalog.models import Products

User = get_user_model()


class Home(ListView):

    def get(self, request):
        context = self.renderPage()
        return render(request, 'users_page/authorization.html', context=context)


class Register(ListView):

    def post(self, request, *args, **kwargs):
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.cleaned_data

            email = new_user['email']
            if not User.objects.filter(email=email):
                self.errors = []
                first_name = new_user['first_name']
                last_name = new_user['last_name']
                phone = new_user['phone'].as_e164
                password = base64.b64encode(
                    str(new_user['password']).encode('utf-8')).decode('utf-8')

                user = User.objects.create(first_name=first_name, last_name=last_name,
                                           phone=phone, email=email, password=password, username=last_name+first_name)
                user.save()
                self.success.append(f'Користувач створений')

            else:
                self.errors.append('Користувач з таким email вже існує')
        else:
            self.errors.append('Користувач з таким телефоном вже створений')

        return redirect(request.META.get('HTTP_REFERER'))


class LoginPhone(ListView):

    def post(self, request, *args, **kwargs):
        phone_form = UserPhoneLogin(request.POST)

        if phone_form.is_valid():
            user = phone_form.cleaned_data
            phone = user['phone']
            password = base64.b64encode(
                str(user['password']).encode('utf-8')).decode('utf-8')
            user_auth = None

            try:
                user_auth = User.objects.get(phone=phone, password=password)
                self.errors = []
            except (AttributeError, User.DoesNotExist):
                self.errors.append('Такого користувача не існує')

            if user_auth is not None:
                login(request, user_auth,
                      backend='django.contrib.auth.backends.ModelBackend')
                self.success.append(
                    f'Користувач {user_auth.first_name} {user_auth.last_name}')
        else:
            self.errors.append('Такого користувача не існує')

        return redirect(request.META.get('HTTP_REFERER'))


class LoginEmail(ListView):

    def post(self, request):
        email_form = UserEmailLogin(request.POST)

        if email_form.is_valid():
            user = email_form.cleaned_data
            email = user['email']
            password = base64.b64encode(
                str(user['password']).encode('utf-8')).decode('utf-8')
            user_auth = None

            try:
                user_auth = User.objects.get(email=email, password=password)
                self.errors = []
            except (AttributeError, User.DoesNotExist):
                self.errors.append('Такого користувача не існує')

            if user_auth is not None:
                login(request, user_auth,
                      backend='django.contrib.auth.backends.ModelBackend')
                self.success.append(
                    f'Користувач {user_auth.first_name} {user_auth.last_name}')
        else:
            self.errors.append('Такого користувача не існує')

        return redirect(request.META.get('HTTP_REFERER'))


def logout_acc(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))


def addbin(request, id):
    bin = Products.objects.get(id=id)
    user = User.objects.get(id=request.user.id)
    user.basket.add(bin)

    return render(request, 'users_page/partials/bin.html', context={'bin': user.basket})


def del_bin_item(request, id):
    bin = Products.objects.get(id=id)
    user = User.objects.get(id=request.user.id)
    user.basket.remove(bin)

    return render(request, 'users_page/partials/bin.html', context={'bin': user.basket})
