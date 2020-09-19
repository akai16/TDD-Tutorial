from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # Iara has heard about a cool new online to-do app.
    # She goes to check out its homepage
    self.browser.get('http://localhost:8000')

    # She notices the page title and header mention to-do lists
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')

    # She is invited to enter a to-do item straight away


    # She type "Buy peacock feathers" into a text box
    # (Iara's hobby is tyinmh fly-fishing lures)

    # When she hits enter, the page updates, and now the page lists:
    # "1: Buy peacock feathers" as an item in a to-do list
    
    # There is still a text box inviting hear to add another item.
    # She enters "Use peacock feathers" as an item in a to-do list.

    # The page updates again, and now shows both items on her list

    # Iara wonders whether the site will remember her list.
    # The she sees that the site has generated a unique url for her
    # There is some explanatory text to that effect.

    # She visits that URL - her to-do list is still here.

    # Satisfied, she goes back to sleep.


if __name__ == '__main__':
  unittest.main()