from tkinter import NW
import unittest

from linked_list import Node, LinkedList

class ListTest(unittest.TestCase):
    def test_emptly_list_head_none(self):
        lst = LinkedList()
        self.assertEqual(lst.head, None)

    def test_append_on_empty_list(self):
        lst = LinkedList()
        lst.append('data')
        self.assertEqual(lst.head.data, 'data')

    def test_append_on_non_empty_list(self):
        lst = LinkedList()
        lst.append('data')
        lst.append('2nd data')
        self.assertEqual(lst.head.next.data, '2nd data')

if __name__ == "__main__":
    unittest.main()