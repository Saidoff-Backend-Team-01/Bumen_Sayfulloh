from django.urls import reverse

from news.models import News

# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.utils import timezone

# class TestNewsListView(APITestCase):
#     url = reverse('news:news_list')

#     def setUp(self):
#         pass

#     def test_news(self):
#         url = reverse('news:news_list')
#         data = {
#             "image": "TestImage",
#             "title": "TestTitle",
#             "description": "TestDescription",
#             "is_publish": "True",
#                 }
#         response = self.client.post(url, data, format="json")
#         print(response)
#         count = News.objects.count()
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(count, 1)
