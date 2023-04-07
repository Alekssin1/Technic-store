from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users_page import views


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, views.Home)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, views.Register)

    def test_login_phone_url_resolves(self):
        url = reverse('login_phone')
        self.assertEqual(resolve(url).func.view_class, views.LoginPhone)

    def test_login_email_url_resolves(self):
        url = reverse('login_email')
        self.assertEqual(resolve(url).func.view_class, views.LoginEmail)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, views.logout_acc)

    def test_add_bin_url_resolves(self):
        url = reverse('addBin', args=[1])
        self.assertEqual(resolve(url).func, views.addbin)

    def test_del_bin_item_url_resolves(self):
        url = reverse('dellBin', args=[1])
        self.assertEqual(resolve(url).func, views.del_bin_item)

    def test_add_count_bin_url_resolves(self):
        url = reverse('addCountBin', args=[1])
        self.assertEqual(resolve(url).func, views.addCountBin)

    def test_del_count_bin_url_resolves(self):
        url = reverse('delCountBin', args=[1])
        self.assertEqual(resolve(url).func, views.delCountBin)