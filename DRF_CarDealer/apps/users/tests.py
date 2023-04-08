# from .models import Client
# from django.test import TestCase
# from django.urls import reverse
#
# class SignupPageTests(TestCase):
# 	def setUp(self):
# 	url = reverse('signup')
# 	self.response = self.client.get(url)
#
# 	def test_signup_template(self):
# 		self.assertEqual(self.response.status_code, 200) self.assertTemplateUsed(self.response, 'registration/signup.html')
# 		self.assertContains(self.response, 'Sign Up')
# 		self.assertNotContains(
# 	self.response, 'Hi there! I should not be on the page.')