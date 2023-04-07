# from django.test import RequestFactory, TestCase
# from django.urls import reverse
# from catalog.models import Products, ProductsType, ProductsBrand
# from catalog.views import AboutProduct, ProductComparison, FilterProductsJson


# class AboutProductViewTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.product_type = ProductsType.objects.create(type='test_type')
#         self.brand = ProductsBrand.objects.create(brand="test_brand")
#         self.product = Products.objects.create(
#             title='Test Product',
#             price=99.99,
#             type=self.product_type,
#             brand=self.brand,
#             amount=10,
#         )

#     def test_about_product_view(self):
#         url = reverse('catalog:about_product', kwargs={'id': self.product.id})
#         request = self.factory.get(url)
#         response = AboutProduct.as_view()(request, id=self.product.id)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'catalog/aboutProduct.html')
#         self.assertContains(response, self.product.title)
#         self.assertContains(response, self.product.price)
#         self.assertContains(response, self.product.brand)


# class ProductComparisonViewTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()

#     def test_product_comparison_view(self):
#         url = reverse('catalog:product_comparison')
#         request = self.factory.get(url)
#         response = ProductComparison.as_view()(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'catalog/productComparison.html')


# class FilterProductsJsonViewTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()

#     def test_filter_products_json_view(self):
#         url = reverse('catalog:filter_products_json',
#                       kwargs={'type': 'test_type'})
#         request = self.factory.get(url)
#         response = FilterProductsJson.as_view()(request, type='test_type')
#         self.assertEqual(response.status_code, 200)
