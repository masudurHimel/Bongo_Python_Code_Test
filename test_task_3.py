import unittest
from task_3 import Node, lca, find_depth

class TestTask3(unittest.TestCase):
    
    root = Node(1, None)
    node2 = Node(2,root)
    node3 = Node(3,root)
    node4 = Node(4,node2)
    node5 = Node(5,node2)
    node6 = Node(6,node3)
    node7 = Node(7,node3)
    node8 = Node(8,node4)
    node9 = Node(9,node4)
    node10 = Node(10,node7)

    def test_lca(self):
        #for testing regular stated value

        self.assertEqual(lca(self.node6,self.node7), 3)
        self.assertEqual(lca(self.node3,self.node7), 3)
        self.assertEqual(lca(self.node10,self.node7), 7)
        self.assertEqual(lca(self.node8,self.node10), 1)
        self.assertEqual(lca(self.root,self.node10), 1)
        self.assertEqual(lca(self.node10,self.node10), 10)
        
    
    def test_find_depth(self):
        #for testing regular stated value
        self.assertEqual(find_depth(self.node10), 3)
        self.assertEqual(find_depth(self.node7), 2)
        self.assertEqual(find_depth(self.root), 0)
        self.assertEqual(find_depth(self.node8), 3)

    def test_types(self):
        # Make sure type error are raised when necessary
        self.assertRaises(TypeError,lca,"Hello ","World")
        self.assertRaises(TypeError,lca,self.node3,2)
        self.assertRaises(TypeError,lca,self.node3,"Node")
        
        
        
        
        
        