from django.db import models
from django.urls import reverse


class ProductsImg(models.Model):
    img = models.ImageField(upload_to='uploads/', verbose_name='Зображення')

    class Meta:
        verbose_name = 'Зображення товару'
        verbose_name_plural = 'Зображення товару'

    def __str__(self):
        return self.img.url


class ValueProductAttributes(models.Model):
    
    value = models.CharField(
        max_length=60, verbose_name="Дані про характеристику товару")

    class Meta:
        verbose_name = "Дані про характеристику товару"
        verbose_name_plural = "Дані про характеристику товару"

    def __str__(self):
        return self.value
    


class ProductAttributes(models.Model):
    attribute = models.CharField(
        max_length=150, verbose_name="Характеристика товару")
    value = models.ManyToManyField(ValueProductAttributes)

    class Meta:
        verbose_name = 'Характеристика товару'
        verbose_name_plural = 'Характеристики товару'

    def __str__(self):
        return self.attribute


class ProductsType(models.Model):
    type = models.CharField(max_length=200, default=None,
                            verbose_name='Типи товару')
    characteristic = models.ManyToManyField(
        ProductAttributes, verbose_name='Характеристики товару')

    class Meta:
        verbose_name = 'Типи товару'
        verbose_name_plural = 'Типи товару'

    def __str__(self):
        return self.type


class ProductsBrand(models.Model):
    brand = models.CharField(
        max_length=200, default=None, verbose_name='Бренди')

    class Meta:
        verbose_name = 'Бренди'
        verbose_name_plural = 'Бренди'

    def __str__(self):
        return self.brand


class Products(models.Model):
    title = models.CharField(
        max_length=200, default=None, verbose_name='Назва')
    price = models.DecimalField(
        max_digits=10, decimal_places=0, verbose_name='Ціна')
    discount = models.DecimalField(
        max_digits=10, decimal_places=0, verbose_name='Ціна зі знижкою', default=None, blank=True, null=True)
    img = models.ManyToManyField(ProductsImg, verbose_name='Зображення')
    type = models.ForeignKey(
        ProductsType, on_delete=models.CASCADE, verbose_name='Тип товару')
    brand = models.ForeignKey(
        ProductsBrand, on_delete=models.CASCADE, verbose_name='Бренд')
    amount = models.PositiveSmallIntegerField(
        default=0, verbose_name='Кількість товару')

    class Meta:
        verbose_name = 'Товари'
        verbose_name_plural = 'Товари'

    def get_pk(self):
        return reverse('aboutProduct', kwargs={'id': self.pk})

    def __str__(self):
        return self.title
