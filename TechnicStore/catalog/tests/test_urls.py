from django.test import SimpleTestCase
from django.urls import reverse, resolve
from catalog.views import Catalog, AboutProduct, ProductComparison, FilterProductsJson, SearchProductsJson, Like, add_liked_item, add_comparison_item, Comments


class TestUrls(SimpleTestCase):

    def test_catalog_url_resolves(self):
        url = reverse('catalog')
        self.assertEquals(resolve(url).func.view_class, Catalog)

    def test_about_product_url_resolves(self):
        url = reverse('aboutProduct', args=[1])
        self.assertEquals(resolve(url).func.view_class, AboutProduct)

    def test_product_comparison_url_resolves(self):
        url = reverse('productComparison')
        self.assertEquals(resolve(url).func.view_class, ProductComparison)

    def test_filter_products_json_url_resolves(self):
        url = reverse('filter_ajax', args=['type'])
        self.assertEquals(resolve(url).func.view_class, FilterProductsJson)

    def test_search_products_json_url_resolves(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class, SearchProductsJson)

    def test_like_url_resolves(self):
        url = reverse('like')
        self.assertEquals(resolve(url).func.view_class, Like)

    def test_add_liked_item_url_resolves(self):
        url = reverse('addLike', args=[1])
        self.assertEquals(resolve(url).func, add_liked_item)

    def test_add_comparison_item_url_resolves(self):
        url = reverse('addComparison', args=[1])
        self.assertEquals(resolve(url).func, add_comparison_item)

    def test_catalog2_url_resolves(self):
        url = reverse('catalog2', args=['type'])
        self.assertEquals(resolve(url).func.view_class, Catalog)

    def test_comments_url_resolves(self):
        url = reverse('comment', args=[1])
        self.assertEquals(resolve(url).func.view_class, Comments)
