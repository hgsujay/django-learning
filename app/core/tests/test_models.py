from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_succssful(self):
        """Test creating a user with email is succesful"""
        email = 'test@example.com'
        password = 'Testpass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@EXAMPLE.COM'
        user = get_user_model().objects.create_user(email, 'Test123')
        self.assertEqual(user.email, email.lower())

    def new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "testuser")

    def test_create_new_superuser(self):
        """test create new superuser"""
        user = get_user_model().objects.create_superuser(
            'superuser@example.com',
            'test123'
        )

        self.assertEqual(user.is_superuser, True)
        self.assertEqual(user.is_staff, True)
