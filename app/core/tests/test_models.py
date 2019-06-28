from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test if email is successful"""
        email = 'adwx1973@gmail.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test if email is normalized"""
        email = 'adwx1973@GMAIL.com'
        user = get_user_model().objects.create_user(
            email,
            '123456'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test if no email is invaild"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123456')

    def test_create_new_superuser(self):
        """test creating a super user"""
        user = get_user_model().objects.create_superuser(
            'adwx1973@GMAIL.com',
            '123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
