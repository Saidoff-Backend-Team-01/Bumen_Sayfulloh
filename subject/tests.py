from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Subject


def test_get_subject(self):
        data = Subject.objects.create(name="Test Name", subject_type="LOCAL", subject_title="Test Title")
        url = reverse("subject:subjects")
        response = self.client.get(url)
        count = Subject.objects.count()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(count, 1)