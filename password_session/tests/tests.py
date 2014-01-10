from django.test import TestCase

try:
    from django.contrib.auth import get_user_model
except ImportError:  # for Django 1.3 compatibility
    from django.contrib.auth.models import User as OldUser
    get_user_model = lambda: OldUser

User = get_user_model()


class PasswordSessionTest(TestCase):
    def test_invalidate_session_after_change_password(self):
        # Create user
        user = User.objects.create_user(email='albert@tugushev.ru', username='albert', password='qwe123')
        user.is_superuser = True
        user.is_staff = True
        user.save()

        # Log in
        response = self.client.post('/admin/', follow=True, data={'username': 'albert',
                                                                  'password': 'qwe123',
                                                                  'this_is_the_login_form': 1,
                                                                  'next': '/admin/'},)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'this_is_the_login_form')

        # Change password
        user.set_password('123qwe')
        user.save()

        # Check for log in page
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'this_is_the_login_form')