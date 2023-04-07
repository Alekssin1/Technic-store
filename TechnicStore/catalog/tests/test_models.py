from django.test import TestCase
from catalog.models import ProductsType, ProductsBrand, Products, ProductAttributes, ValueProductAttributes, ProductsImg


class ProductsTypeTest(TestCase):

    def setUp(self):
        self.type = ProductsType.objects.create(type="Смартфони")

    def test_type_str(self):
        self.assertEqual(str(self.type), "Смартфони")


class ProductsBrandTest(TestCase):

    def setUp(self):
        self.brand = ProductsBrand.objects.create(brand="Apple")

    def test_brand_str(self):
        self.assertEqual(str(self.brand), "Apple")


class ProductsTest(TestCase):

    def setUp(self):
        self.type = ProductsType.objects.create(type="Смартфони")
        self.brand = ProductsBrand.objects.create(brand="Apple")
        self.product = Products.objects.create(
            title="Iphone 13", price=600, type=self.type, brand=self.brand, amount=10)

    def test_product_str(self):
        self.assertEqual(str(self.product), "Iphone 13")


class ProductAttributesTest(TestCase):

    def setUp(self):
        self.value1 = ValueProductAttributes.objects.create(value="8 GB")
        self.value2 = ValueProductAttributes.objects.create(value="512 GB")
        self.attribute = ProductAttributes.objects.create(attribute="Memory")
        self.attribute.value.set([self.value1, self.value2])

    def test_attribute_str(self):
        self.assertEqual(str(self.attribute), "Memory")


class ValueProductAttributesTest(TestCase):

    def setUp(self):
        self.value = ValueProductAttributes.objects.create(value="8 GB")

    def test_value_str(self):
        self.assertEqual(str(self.value), "8 GB")


class ProductsImgTest(TestCase):

    def setUp(self):
        self.img = ProductsImg.objects.create(
            img="/static/img/temp/xbox1.jpg")

    def test_img_str(self):
        self.assertEqual(str(self.img), "/static/img/temp/xbox1.jpg")
