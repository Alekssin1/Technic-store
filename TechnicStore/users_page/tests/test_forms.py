from django.test import TestCase
from users_page.forms import UserRegistrationForm, UserEmailLogin, UserPhoneLogin
from users_page.models import User


class UserRegistrationFormTestCase(TestCase):
    def test_form_valid_data(self):
        form = UserRegistrationForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '+380965194692',
            'email': 'john.doe@example.com',
            'password': 'pass123'
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


class UserEmailLoginFormTestCase(TestCase):
    def test_form_valid_data(self):
        form = UserEmailLogin(data={
            'email': 'john.doe@example.com',
            'password': 'pass123'
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = UserEmailLogin(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


class UserPhoneLoginFormTestCase(TestCase):
    def test_form_valid_data(self):
        form = UserPhoneLogin(data={
            'phone': '+380965194692',
            'password': 'pass123'
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = UserPhoneLogin(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
