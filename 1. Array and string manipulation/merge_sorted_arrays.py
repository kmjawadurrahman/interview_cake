import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    if not my_list and not alices_list:
        return []

    if not my_list:
        return alices_list

    if not alices_list:
        return my_list

    merged_list = my_list.copy()
    for alices_item in alices_list:
        for my_idx, item in enumerate(merged_list):
            if alices_item < item:
                merged_list.insert(my_idx, alices_item)
                break
        else:
            merged_list.append(alices_item)

    return merged_list


















# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
