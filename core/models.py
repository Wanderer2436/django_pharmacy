from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Category(models.Model):
    name = models.CharField('Название категории', max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название товара', max_length=50, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    type = models.CharField('Форма выпуска', max_length=50, blank=True)
    manufacturer = models.CharField('Производитель', max_length=20, blank=True, null=True)
    country = models.CharField('Страна производителя', max_length=15, blank=True, null=True)
    price = models.IntegerField('Цена товара')
    photo = models.ImageField('Изображение товара', upload_to='products/', blank=True)
    indications_for_use = models.TextField('Показания к применению', blank=True)
    mode_of_application = models.TextField('Способ применения', blank=True)
    composition = models.TextField('Состав', blank=True)
    contraindications = models.TextField('Противопоказания', blank=True)

    def __str__(self):
        return self.name


class Pharmacy(models.Model):
    name = models.CharField('Название аптеки', max_length=25)
    street = models.CharField("Улица", max_length=50, blank=True, null=True)
    house = models.IntegerField("Номер дома", blank=True, null=True)
    phone = models.IntegerField("Номер телефона", blank=True, null=True)
    photo = models.ImageField('Изображение аптеки', upload_to='pharmacies/', blank=True)
    opening_time = models.TimeField('Время открытия', default='9:00', blank=True)
    closing_time = models.TimeField('Время закрытия', default='21:00', blank=True)

    def __str__(self):
        return self.name


class Available(models.Model):
    pharmacy = models.ForeignKey('Pharmacy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Количество')

    def __str__(self):
        return f'{self.pharmacy} {self.product} {self.quantity}'


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Корзина для {self.user}'


class CartItem(models.Model):
    cart = models.OneToOneField(Cart, null=True, related_name='items', blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(blank=True, default=0)
    total_price = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_price = (self.price * self.quantity)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.cart}, {self.product}'

    def get_total_price_of_items(self):
        qty = self.items.all().aggregate(Sum('quantity'))
        return qty['sum']



