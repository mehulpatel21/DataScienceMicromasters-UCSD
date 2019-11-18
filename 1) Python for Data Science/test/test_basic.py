import unittest2


class TestBasic(unittest2.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        string = "What up"
        self.assertEqual(string.split(), ['What', 'up'])
        with self.assertRaises(TypeError):
            string.split(2)


if __name__ == "__main__":
    unittest2.main()
