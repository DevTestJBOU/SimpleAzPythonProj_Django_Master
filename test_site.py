# ORIGINAL
#from django.test import TestCase

#class HelloWorldTest(TestCase):
#    def test_site(self):
#        self.assertEqual(1, 1)
        
from django.test import TestCase

class HelloWorldTest(TestCase):
    def test_site(self):
        self.assertEqual(1, 1)
        self.assertEqual(1, 2)
        self.assertEqual(2, 1)
        self.assertEqual(2, 2)





