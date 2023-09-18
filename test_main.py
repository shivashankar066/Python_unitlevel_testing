import unittest
from main import testing
test_obj = testing()


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(test_obj.add(1, 2), 3)

