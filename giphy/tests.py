from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from .models import Gif

from accounts.models import CustomUser


class GifModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser(username="bob")
        self.user.save()
        self.g = Gif(
            owner=self.user,
            image_id="12345"
        )

    def test_gif_image_id_cant_be_blank(self):
        g = Gif(
            owner=self.user
        )
        g.save()
        self.assertRaises(ValidationError, g.full_clean)

    def test_gif_fails_if_image_orig_url_not_valid_url(self):
        self.g.image_orig_url = "foo"
        self.g.image_200_url = "http://foo.com"
        self.g.save()
        self.assertRaises(ValidationError, self.g.full_clean)

    def test_gif_passes_if_image_orig_url_valid_url(self):
        """
        This tests both url fields since setting image_200_url
        to an invalid url would cause this to fail as shown by
        the test below

        :return:
        """
        self.g.image_orig_url = "http://foo.com"
        self.g.image_200_url = "http://foo.com/200"
        self.g.save()
        self.g.full_clean()

    def test_gif_fails_if_image_200_url_not_valid(self):
        self.g.image_orig_url = "http://foo.com"
        self.g.image_200_url = "foo"
        self.g.save()
        self.assertRaises(ValidationError, self.g.full_clean)


class GiphyViewsTest(TestCase):

    def test_index_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, '/accounts/login/?next=/giphy/')

    def test_search_redirect_if_not_logged_in(self):
        response = self.client.get(reverse("search"))
        self.assertRedirects(response, '/accounts/login/?next=/giphy/search/')
