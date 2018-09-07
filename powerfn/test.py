import unittest

from powerfn.power import multiply_items

class multiply(unittest.TestCase):

    def setUp(self):
        pass
  
    def test_power_works(self):
       self.assertEqual(multiply_items(2,3),8, 'answer should be 8')  









if '__name__' == '__main__':
  unittest.main