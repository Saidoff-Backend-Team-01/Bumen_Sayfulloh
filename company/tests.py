from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse


class TestContactWithUsView(APITestCase):

    def setUp(self):
        pass

    def test_happy(self):
        url = reverse('contact_with_us')
        data = {
            "name": "TestName",
            "phone_number": "+998919209292",
            "message": "TestMesssage"
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['name'], 'TestName')
        self.assertEquals(list(response.data.keys()), ['name', 'phone_number', 'message'])


class TestContactsView(APITestCase):
    def setUp(self):
        pass
    
    def test_happy(self):
        url = reverse('contacts')
        data = {
            "email": "TestEmail",
            "phone_number": "+998901791459",
            "location": "TestLocation",
            "address":"TestAddress"
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['email'], 'TestEmail')
        self.assertEquals(list(response.data.keys()), ['address', 'phone_number', 'email', 'location'])