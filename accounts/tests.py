from django.test import TestCase
from .models import CustomUser


class CustomUserTest(TestCase):

    def test_string_representation(self):
        """
        Testing the __str__ method we made works as expected

        :return:
        """
        user = CustomUser(username="test_guy")
        self.assertEqual(str(user), user.username)
