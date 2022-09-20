from django.test import Client, TestCase
from django.urls import reverse


# Create your tests here.
class Test(TestCase): 
    def test_app_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEquals(response.status_code,200)

    def test_app_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEquals(response.status_code,200)

    def test_app_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEquals(response.status_code,200)




