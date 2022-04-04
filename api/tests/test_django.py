from django.test import TestCase
from django.urls import reverse, resolve 
from api.views import GuessView
# Create your tests here.


# class TestURL(TestCase):

#     def test_home_url_is_resolved(self):
#         url = reverse('api:home')
#         self.assertEquals(resolve(url).func, GuessView.as_view())