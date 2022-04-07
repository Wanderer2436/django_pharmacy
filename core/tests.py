from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from core import models


class ProductSearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        category1 = models.Category.objects.create(name='TestCat1')
        category2 = models.Category.objects.create(name='TestCat2')
        self.product1 = models.Product.objects.create(name='Test1', category=category1, price=10)
        self.product2 = models.Product.objects.create(name='Test2', category=category2, price=25)

    def testWithoutParams(self):
        response = self.client.get(reverse('core:catalog'))
        self.assertSequenceEqual(
            list(response.context['products']),
            list(models.Product.objects.all()),
            'При поиске без параметров должны выводиться все продукты',
        )

    def testSearchByName(self):
        response = self.client.get(reverse('core:catalog'), data={'name': 'Test1'})
        self.assertEqual(1, response.context['products'].count())
        self.assertEqual(
            'Test1',
            response.context['object_list'].first().name,
        )

    def testProductDetail(self):
        response = self.client.get('/catalog/product/1/')
        self.assertEqual(response.status_code, 200)


class PharmacySearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.pharmacy1 = models.Pharmacy.objects.create(name='Test1')
        self.pharmacy2 = models.Pharmacy.objects.create(name='Test2')

    def testWithoutParams(self):
        response = self.client.get(reverse('core:pharmacy'))
        self.assertSequenceEqual(
            list(response.context['object_list']),
            list(models.Pharmacy.objects.all()),
            'При поиске без параметров должны выводиться все аптеки',
        )

    def testSearchByName(self):
        response = self.client.get(reverse('core:pharmacy'), data={'name': 'Test1'})
        self.assertEqual(2, response.context['object_list'].count())
        self.assertEqual(
            'Test1',
            response.context['object_list'].first().name,
        )
