from django.urls import reverse
from rest_framework.test import APITestCase

from common.models import Media

from .models import Group, User, UserMessage


class TestAccount(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="JohnDoe",
            first_name="John",
            last_name="Doe",
            birth_date="1990-01-01",
        )
        self.group = Group.objects.create(name="TestGroup")
        self.media = Media.objects.create(file="path/to/file")

    def test_get_profile(self):
        User.objects.create(
            first_name="TestName", last_name="TestLastName", birth_date="1990-01-01"
        )
        url = reverse("account:profile")
        response = self.client.get(url)
        count = User.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 2)

    def test_get_group(self):
        self.group.users.set([self.user])
        url = reverse("account:group")
        response = self.client.get(url)
        count = Group.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 1)

    def test_user_message(self):
        UserMessage.objects.create(
            user=self.user, message="TestUser", file=self.media, group=self.group
        )
        url = reverse("account:profile_message")
        response = self.client.get(url)
        count = UserMessage.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 1)
