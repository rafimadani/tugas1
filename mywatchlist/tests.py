from urllib3 import response
from django.test import TestCase
from django.test import Client

# Create your tests here.

class UnitTest(TestCase):
    def test_mywatchlist_html_if_exist(self):
        response = Client().get('/mywatchlist/htmlview/')
        self.assertEqual(response.status_code,200)
        
    def test_mywatchlist_json__if_exist(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_xml_if_exist(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    
    
  

