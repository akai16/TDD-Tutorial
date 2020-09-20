from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


class HomePageTest(TestCase):

  def test_home_page_returns_correct_html(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'lists/home.html')

    # Let's check if our response has an input with attribute name
    html = response.content.decode('utf-8')
    self.assertIn(
      'name="item_text"', 
      html, 
      'Missing attribute \'name\' on input for adding new To-Do'
    )

  def test_can_save_a_POST_request(self):
    response = self.client.post('/', data={'item_text': 'A new list item'})
    self.assertIn(
      'A new list item', 
      response.content.decode(),
      'To-Do Item was not included into response'
    )
    self.assertTemplateUsed(response, 'lists/home.html')

  