from django.test import TestCase
from catalog.models import Products, ProductsBrand, ProductsType
from users_page.models import User, Bin


class UsersPageModelsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.type = ProductsType.objects.create(type="Смартфони")
        cls.brand = ProductsBrand.objects.create(brand="Apple")
        cls.product = Products.objects.create(
            title='Iphone 13', price=600, type=cls.type, brand=cls.brand, amount=10)

    def test_user_has_phone_number_field(self):
        user = User.objects.create(
            username='testuser', phone='+380965194692', email='test@example.com')
        self.assertEqual(user.phone, '+380965194692')

    def test_user_has_basket_relationship(self):
        user = User.objects.create(
            username='testuser', phone='+380965194692', email='test@example.com')
        bin = Bin.objects.create(product=self.product, count=1)
        user.basket.add(bin)
        self.assertEqual(user.basket.count(), 1)

    def test_user_has_like_relationship(self):
        user = User.objects.create(
            username='testuser', phone='+380965194692', email='test@example.com')
        user.like.add(self.product)
        self.assertEqual(user.like.count(), 1)

    def test_user_has_comparison_relationship(self):
        user = User.objects.create(
            username='testuser', phone='+380965194692', email='test@example.com')
        user.comparison.add(self.product)
        self.assertEqual(user.comparison.count(), 1)

    def test_bin_has_product_relationship(self):
        bin = Bin.objects.create(product=self.product, count=1)
        self.assertEqual(bin.product.title, 'Iphone 13')

    def test_bin_has_count_field(self):
        bin = Bin.objects.create(product=self.product, count=1)
        self.assertEqual(bin.count, 1)
