from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page


class HomePageTest(TestCase):

    def test_home_page_resolves_to_root_url(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)