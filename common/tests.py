# from rest_framework.test import APITestCase
# from django.urls import reverse
# from .models import Media

# class TestMediaView(APITestCase):

#     def setUp(self):
#         pass

#     def test_happy(self):

#         url = reverse('common:media')
#         data = {
#             "type": "TestName",
#             "file": "+998919209292"
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.data['type'], 'TestName')
#         self.assertEqual(list(response.data.keys()), ['type', 'file'])