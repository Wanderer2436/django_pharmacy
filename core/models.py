from django.db import models


class Category(models.Model):
    name = models.CharField('Название категории', max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название товара', max_length=50, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    manufacturer = models.CharField('Производитель', max_length=20, blank=True, null=True)
    country = models.CharField('Страна производителя', max_length=15, blank=True, null=True)
    price = models.IntegerField('Цена товара', max_length=5)
    description = models.TextField('Описание товара', max_length=250, blank=True, null=True)
    photo = models.ImageField('Изображение товара', upload_to='products/', blank=True)

    def __str__(self):
        return self.name


class Pharmacy(models.Model):
    name = models.CharField('Название аптеки', max_length=25)
    street = models.CharField("Улица", max_length=50, blank=True, null=True)
    house = models.IntegerField("Номер дома", blank=True, null=True)
    phone = models.IntegerField("Номер телефона", blank=True, null=True)
    photo = models.ImageField('Изображение аптеки', upload_to='pharmacies/', blank=True)

    def __str__(self):
        return self.name


class Supply(models.Model):
    supplier = models.CharField('Название поставщика', max_length=25)
    pharmacy = models.ForeignKey('Pharmacy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Количество')

    def __str__(self):
        return f'{self.product} {self.quantity}'



