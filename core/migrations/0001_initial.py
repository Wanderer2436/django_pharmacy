# Generated by Django 4.0.3 on 2022-04-05 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название аптеки')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица')),
                ('house', models.IntegerField(blank=True, null=True, verbose_name='Номер дома')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='Номер телефона')),
                ('photo', models.ImageField(blank=True, upload_to='pharmacies/', verbose_name='Изображение аптеки')),
                ('opening_time', models.TimeField(blank=True, default='9:00', verbose_name='Время открытия')),
                ('closing_time', models.TimeField(blank=True, default='21:00', verbose_name='Время закрытия')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название товара')),
                ('type', models.CharField(blank=True, max_length=50, verbose_name='Форма выпуска')),
                ('manufacturer', models.CharField(blank=True, max_length=20, null=True, verbose_name='Производитель')),
                ('country', models.CharField(blank=True, max_length=15, null=True, verbose_name='Страна производителя')),
                ('price', models.IntegerField(verbose_name='Цена товара')),
                ('photo', models.ImageField(blank=True, upload_to='products/', verbose_name='Изображение товара')),
                ('indications_for_use', models.TextField(blank=True, verbose_name='Показания к применению')),
                ('mode_of_application', models.TextField(blank=True, verbose_name='Способ применения')),
                ('composition', models.TextField(blank=True, verbose_name='Состав')),
                ('contraindications', models.TextField(blank=True, verbose_name='Противопоказания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(verbose_name='Отзыв')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pharmacy')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
    ]
