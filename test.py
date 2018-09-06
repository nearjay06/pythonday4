import unittest

from plus import compute_items


class SeeCase (unittest.TestCase):
 def setUp(self):
    pass
 def test_plus_works(self):
  result = compute_items([1,2])
  self.assertEqual(result,3)




if '__name__' == '__main__':
  unittest.main()