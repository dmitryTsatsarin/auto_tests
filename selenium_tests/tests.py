from django.test import TestCase

# Create your tests here.
class MyFirstTest(TestCase):

    def setUp(self):
        pass

    def test_first(self):
        print 'hello'

    def tearDown(self):
        pass