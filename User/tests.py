# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.admin.sites import site
from rest_framework.test import APITestCase

CustomUser = get_user_model()

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            role='admin'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertEqual(user.role, 'admin')
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        admin_user = CustomUser.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123'
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class CustomUserAdminTest(TestCase):
    def test_admin_registration(self):
        # Check if CustomUser is registered in admin
        self.assertIn(CustomUser, site._registry)


class CustomUserAPITest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            password='testpass123',
            role='admin'
        )
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.list_url = reverse('user-list-create')
        self.detail_url = reverse('user-detail', args=[self.user.id])
        self.forgot_url = reverse('forgot-password')

    def test_login_success(self):
        response = self.client.post(self.login_url, {
            'email': 'user@example.com',
            'password': 'testpass123'
        }, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.data)

    def test_login_failure(self):
        response = self.client.post(self.login_url, {
            'email': 'user@example.com',
            'password': 'wrongpass'
        }, format='json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('error', response.data)

    def test_logout(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.data)

    def test_user_list_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_user_list_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 401)

    def test_forgot_password(self):
        response = self.client.post(self.forgot_url, {
            'email': 'user@example.com'
        }, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.data)