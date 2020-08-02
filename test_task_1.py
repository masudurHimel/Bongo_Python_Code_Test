import unittest
from task_1 import print_depth

class TestTask1(unittest.TestCase):
    def test_print_depth(self):
        #for testing regular stated value
        target_value = {"key1": 1,"key2": {"key3": 1,"key4": {"key5": 4}}}
        result = "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3"
        self.assertMultiLineEqual(print_depth(target_value), result)
        
        target_value = {"key1": 1,"key2": {"key3": 1},"key4" : 3}
        result = "key1 1\nkey2 1\nkey4 1\nkey3 2"
        self.assertMultiLineEqual(print_depth(target_value), result)
        
        target_value = {"key1": 1}
        result = "key1 1"
        self.assertMultiLineEqual(print_depth(target_value), result)
        
        target_value = {}
        result = ""
        self.assertMultiLineEqual(print_depth(target_value), result)

        target_value = {"key1": 1,"key2": {"key3": 1,"key4": {"key5": "key6", "key7" : "key8", "key9" : {'key10': 2}}}}
        result = "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nkey7 3\nkey9 3\nkey10 4"
        self.assertMultiLineEqual(print_depth(target_value), result)
    
    def test_types(self):
        # Make sure type error are raised when necessary
        self.assertRaises(TypeError, print_depth, "Hello!!")
        self.assertRaises(TypeError, print_depth, 1234)
        self.assertRaises(TypeError, print_depth, {1,2,3,"Himel"})
        
        
        