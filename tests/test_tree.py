from bst.node import Node
from bst.tree import Tree
import unittest2

class TreeTestCase(unittest2.TestCase):

    def setUp(self):
        self.tree = Tree(Node(9))


    def tearDown(self):
        self.tree = None


    def test_find_node(self):
        self.assertTrue(self.tree.find_node(9, self.tree.root), self.tree.root)
        self.assertFalse(self.tree.find_node(1, self.tree.root), self.tree.root)
        self.assertFalse(self.tree.find_node(15, self.tree.root), self.tree.root)


    def test_contains(self):
        self.assertFalse(self.tree.contains(1, self.tree.root))
        self.assertFalse(self.tree.contains(15, self.tree.root))


    def test_insert(self):
        self.tree.insert(Node(6))
        self.assertTrue(self.tree.contains(6, self.tree.root))


    def test_delete(self):
        self.tree.insert(Node(12))
        self.assertTrue(self.tree.delete(12))  # leaf
        self.assertFalse(self.tree.delete(12))


    def test_find_smaller(self):
        self.tree.insert(Node(4))
        self.tree.insert(Node(2))
        self.tree.insert(Node(6))
        self.tree.insert(Node(15))
        self.assertEqual(list(self.tree.find_smaller(9, self.tree.root)), [4, 2, 6])


    def test_find_bigger(self):
        self.tree.insert(Node(22))
        self.tree.insert(Node(18))
        self.tree.insert(Node(25))
        self.assertEqual(list(self.tree.find_bigger(9, self.tree.root)), [22, 25, 18])


    def test_find_min(self):
        self.tree.insert(Node(2))
        self.tree.insert(Node(18))
        self.tree.insert(Node(4))
        self.assertEqual(self.tree.find_min(self.tree.root).val, 2)


    def test_find_max(self):
        self.tree.insert(Node(2))
        self.tree.insert(Node(18))
        self.tree.insert(Node(4))
        self.tree.insert(Node(13))
        self.assertEqual(self.tree.find_max(self.tree.root).val, 18)


    def test_preorder_traverse(self):
        self.tree.insert(Node(6))
        self.tree.insert(Node(22))
        self.tree.insert(Node(1))
        self.tree.insert(Node(4))
        self.tree.insert(Node(2))
        self.tree.insert(Node(18))
        self.assertEqual(list(self.tree.preorder_traverse(self.tree.root)), [9, 6, 1, 4, 2, 22, 18])


    def test_inorder_traverse(self):
        self.tree.insert(Node(6))
        self.tree.insert(Node(22))
        self.tree.insert(Node(1))
        self.tree.insert(Node(4))
        self.tree.insert(Node(2))
        self.tree.insert(Node(18))
        self.assertEqual(list(self.tree.inorder_traverse(self.tree.root)), [1, 2, 4, 6, 9, 18, 22])


    def test_postorder_traverse(self):
        self.tree.insert(Node(6))
        self.tree.insert(Node(22))
        self.tree.insert(Node(1))
        self.tree.insert(Node(4))
        self.tree.insert(Node(2))
        self.tree.insert(Node(18))
        self.assertEqual(list(self.tree.postorder_traverse(self.tree.root)), [2, 4, 1, 6, 18, 22, 9])
