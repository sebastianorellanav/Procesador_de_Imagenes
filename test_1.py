import unittest
import moduloTest


class TestMyModule(unittest.TestCase):

    def test_1(self):
        self.assertEqual(moduloTest.Test1(), 1)

if __name__ == "__main__":
   unittest.main()