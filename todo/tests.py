from django.test import TestCase

# Create your tests here.
class SampleTestCace(TestCase):
    def test_sample1(self):
        self.assertEqual(1 + 2, 3)