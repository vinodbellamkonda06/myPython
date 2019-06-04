import unittest


class Testing(unittest.TestCase):

    def test_string(self):
        a = 'vinod'
        b = 'vinod'
        self.assertEqual(a, b)

    def test_string(self):
        a = 'vinod'
        b = 'vinodh'
        self.assertNotEqual(a, b)


if __name__ == '__main__':
    unittest.main()
