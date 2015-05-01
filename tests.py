import unittest
import challenges


class ConditionalsTests(unittest.TestCase):

    def test_is_ten(self):
        self.assertEqual(True, challenges.is_ten(10))
        self.assertEqual(False, challenges.is_ten(4))

    def test_bigger_than_ten(self):
        self.assertEqual(False, challenges.bigger_than_ten(10))
        self.assertEqual(False, challenges.bigger_than_ten(0))
        self.assertEqual(True, challenges.bigger_than_ten(100))

    def test_smaller_than_ten(self):
        self.assertEqual(False, challenges.smaller_than_ten(10))
        self.assertEqual(True, challenges.smaller_than_ten(0))
        self.assertEqual(False, challenges.smaller_than_ten(100))

    def test_return_bigger(self):
        self.assertEqual(10, challenges.return_bigger(0, 10))
        self.assertEqual(0, challenges.return_bigger(0, 0))

    def test_is_positive(self):
        self.assertEqual(True, challenges.is_positive(10))
        self.assertEqual(False, challenges.is_positive(-10))

    def test_is_negative(self):
        self.assertEqual(False, challenges.is_negative(10))
        self.assertEqual(True, challenges.is_negative(-10))

    def test_is_divisable_by_two(self):
        pass

    def test_is_divisable_by_five(self):
        pass

    def test_is_divisable_by_ten(self):
        pass

    def test_is_divisable_by_ten_and_five(self):
        pass

    def test_Is_str_longer_than_ten(self):
        pass

    def test_is_int(self):
        pass

    def test_is_str(self):
        pass

    def test_is_list(self):
        pass


class ListTest(unittest.TestCase):

    def test_does_list_contain_Int(self):
        pass

    def test_does_list_contain_str(self):
        pass

    def test_is_list_empty(self):
        pass

    # more tests - filtering lists, changing values etc..

# etc. More domains -  working with strings, dictionaries, file i/o etc.


def main():
    unittest.main()

if __name__ == '__main__':
    main()
