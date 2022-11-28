# from django.urls import reverse_lazy
# from rest_framework.test import APITestCase
#
# from .models import *
#
#
# class TestCategory(APITestCase):
#     url = reverse_lazy('categories')
#
#     def test_list(self):
#         category = Category.objects.create(name="Tests")
#
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         excepted = [
#             {
#                 'id': category.pk,
#                 'name': category.name
#             }
#         ]
#         self.assertEqual(excepted, response.json())
#
#     # def test_unique_name(self):
#     #     self.assertFalse(Category.objects.exist())
#     #     response = self.client.post(self.url, data={'name': "Tests"})
#     #     self.assertEqual(response.status_code, 405)
#     #     self.assertFalse(Category.objects.exist())
