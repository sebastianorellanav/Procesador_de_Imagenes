import unittest
import moduloTest


class TestMyModule(unittest.TestCase):

    def test_2(self):
        self.assertEqual(moduloTest.Test2(), 1)

if __name__ == "__main__":
   unittest.main()