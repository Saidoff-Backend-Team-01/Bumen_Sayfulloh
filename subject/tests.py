from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Subject, SubjectTitle, Category

class TestSubjectView(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.subject_title = SubjectTitle.objects.create(
            name="Test Title",
            category=self.category
        )
        self.subject = Subject.objects.create(
            name="TestName",
            subject_type="local",
            subject_title=self.subject_title
        )

    def test_happy(self):
        url = reverse("subject:subjects")  # Bu yerda URL-ni to'g'ri ekanligiga ishonch hosil qiling
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["name"], "TestName")
        self.assertEqual(
            list(response.data[0].keys()), ["name", "subject_type", "subject_title"])
