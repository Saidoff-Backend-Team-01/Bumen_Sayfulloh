from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from common.models import Media
from company.models import FAQ, AppInfo, Contacts, ContactUsWeb, PrivacyPolicy, SocialMedia, Sponsor


class TestCompanyViews(APITestCase):

    def setUp(self):
        pass

    def test_contacts_us(self):
        url = reverse("company:contact_with_us")
        data = {
            "name": "TestName",
            "phone_number": "+998930682911",
            "message": "Test message",
        }
        response = self.client.post(url, data, format="json")
        print(response)
        count = ContactUsWeb.objects.count()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(count, 1)

    def test_create_contacts(self):
        ad = Contacts.objects.create(
            address="test",
            phone_number="+998930682911",
            email="test@example.com",
            location="https://t.me/IT_RustamDevPythonMy",
        )
        url = reverse("company:contact")
        response = self.client.get(url)
        print(response)
        count = Contacts.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 1)

    def test_get_faq(self):
        data = FAQ.objects.create(question="Test Question", answer="Test Answer")
        url = reverse("company:faqs")
        response = self.client.get(url)
        count = FAQ.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 1)

    def test_social_media(self):
        data = SocialMedia.objects.create(
            telegram="https://t.me/IT_RustamDevPythonMy",
            facebook="https://t.me/IT_RustamDevPythonMy",
            instagram="https://t.me/IT_RustamDevPythonMy",
            linkedin="https://t.me/IT_RustamDevPythonMy",
        )
        url = reverse("company:socialmedia")
        response = self.client.get(url)
        count = SocialMedia.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 1)

    def test_app_info(self):
        data = AppInfo.objects.create(
            title="Test App", desc="This is a test app description."
        )
        url = reverse("company:appinfo")
        response = self.client.get(url)
        count = AppInfo.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 1)

    def test_privacy_policy(self):
        data = PrivacyPolicy.objects.create(text="This is a test privacy policy.")
        url = reverse("company:privacypolicy")
        response = self.client.get(url)
        count = PrivacyPolicy.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 1)

    def test_sponsor(self):
        test_image = SimpleUploadedFile(
            name="software.png",
            content=open("media/software.png", "rb").read(),
            content_type="image/png",
        )
        media = Media.objects.create(file=test_image)
        data = Sponsor.objects.create(
            image=media,
            url="https://i.pinimg.com/236x/0b/11/81/0b11814a2a85126c755ce96d88593e1c.jpg",
        )
        url = reverse("company:sponsor")
        response = self.client.get(url)
        count = Sponsor.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 1)