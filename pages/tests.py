from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView # new

# Create your tests here.
class HomePageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)


    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)



    def test_hompage_template(self): # new
        self.assertTemplateUsed(self.response, 'home.html')


    def test_homepage_contains_correct_html(self): # new
        self.assertContains(self.response, 'HomePage')

    def test_homepage_dose_not_contain_incorrect_hml(self):
        self.assertNotContains(self.response, 'Hi there! I shold not be on the page.')

    def test_homepage_url_resolves_homepageview(self): # new
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
