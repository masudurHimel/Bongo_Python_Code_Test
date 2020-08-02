import unittest
from task_2 import print_depth, Person, process_dict

class TestTask2(unittest.TestCase):
    def test_print_depth(self):
        # for testing regular stated value
        # first attempt
        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a)
        target_value = { "key1": 1, "key2": { "key3": 1, "key4": { "key5": 4, "user": person_b}}}
        
        result = "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nuser 3\nfirst_name 4\nlast_name 4\nfather 4\nfirst_name 5\nlast_name 5\nfather 5"
        self.assertMultiLineEqual(print_depth(target_value), result)

        # second attempt
        person_a = Person("User", "1", "New_user")
        person_b = Person("User", "2", person_a)
        person_c = Person("New_user", "3", person_b)
        target_value = { "key1": 1, "key2": { "key3": 1, "key4": { "key5": 4, "user": person_b}}, "New_User" : person_c}
        
        result = "key1 1\nkey2 1\nNew_User 1\nfirst_name 2\nlast_name 2\nfather 2\nkey3 2\nkey4 2\nfirst_name 3\nlast_name 3\nfather 3\nkey5 3\nuser 3\nfirst_name 4\nlast_name 4\nfather 4\nfirst_name 4\nlast_name 4\nfather 4\nfirst_name 5\nlast_name 5\nfather 5"
        self.assertMultiLineEqual(print_depth(target_value), result)

    def test_process_dict(self):
        # for testing regular stated value
        # first attempt
        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a)
        target_value = { "key1": 1, "key2": { "key3": 1, "key4": { "key5": 4, "user": person_b}}}
        result = {'key1': 1, 'key2': {'key3': 1, 'key4': {'key5': 4, 'user': {'first_name': 'User', 'last_name': '2', 
        'father': {'first_name': 'User', 'last_name': '1', 'father': None}}}}}
        process_dict(target_value)
        self.assertDictEqual(target_value, result)

        # second attempt
        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a)
        person_c = Person("New_user", "3", person_b)
        target_value = { "key1": 1, "key2": { "key3": 1, "key4": { "key5": 4, "user": person_b}}, "New_User" : person_c}
        
        result = {'key1': 1, 'key2': {'key3': 1, 'key4': {'key5': 4, 'user': {'first_name': 'User', 'last_name': '2', 
        'father': {'first_name': 'User', 'last_name': '1', 'father': None}}}}, 
        'New_User': {'first_name': 'New_user', 'last_name': '3', 
        'father': {'first_name': 'User', 'last_name': '2', 
        'father': {'first_name': 'User', 'last_name': '1', 'father': None}}}}
        
        process_dict(target_value)
        self.assertDictEqual(target_value, result)


    def test_types(self):
        # Make sure type error are raised when necessary
        # for print_depth function
        self.assertRaises(TypeError, print_depth, "Hello!!")
        self.assertRaises(TypeError, print_depth, 1234)
        self.assertRaises(TypeError, print_depth, {1,2,3,"Himel"})
        # for process_dict function 
        self.assertRaises(TypeError, process_dict, "Hello!!")
        self.assertRaises(TypeError, process_dict, 1234)
        self.assertRaises(TypeError, process_dict, {1,2,3,"Himel"})


        
        
        