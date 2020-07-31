import unittest
import moduloTest


class TestMyModule(unittest.TestCase):

    def test_3(self):
        self.assertEqual(moduloTest.Test3(), 1)

if __name__ == "__main__":
   unittest.main()