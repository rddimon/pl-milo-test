import unittest

from django.test import RequestFactory
from django.urls import reverse

from apps.account import views
from apps.account.models import User


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.test_user = User.objects.create_user('example', 'example@mail.com', 'Milotest123')

    def test_account(self):
        request = self.factory.get(reverse('account_user_list'))
        response = views.user_list(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.post(reverse('account_user_new'),
                                    {'username': 'example', 'password': 'Milotest123', 'password2': 'Milotest123'})
        response = views.user_new(request)
        self.assertEqual(response.status_code, 200)

        request = self.factory.get(reverse('account_user_detail', args=[self.test_user.id]))
        response = views.user_detail(request, self.test_user.id)
        self.assertEqual(response.status_code, 200)

        request = self.factory.post(reverse('account_user_detail', args=[self.test_user.id]), {'first_name': 'example'})
        response = views.user_detail(request, self.test_user.id)
        self.assertEqual(response.status_code, 200)

        request = self.factory.post(reverse('account_user_delete', args=[self.test_user.id]))
        response = views.user_delete(request, self.test_user.id)
        self.assertEqual(response.status_code, 302)

        request = self.factory.get(reverse('account_user_list_download'))
        response = views.user_list_download(request)
        self.assertEqual(response.status_code, 200)
