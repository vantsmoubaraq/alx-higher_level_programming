#!/usr/bin/python3

import unittest
from models import base

Base = base.Base

class test_base(unittest.TestCase):
    def test_module_doc(self):
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_doc(self):
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_no_id(self):
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)

    def test_with_id(self):
        b = Base(22)
        self.assertEqual(b.id, 22)

    def test_with_or_without(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base(14)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 14)

    def test_multiple_no_id(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_multiple_with_wthout_id(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base(98)
        b4 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 98)
        self.assertEqual(b4.id, 3)
    
    def test_isinstance_of(self):
        Base._Base__nb_objects = 0
        b = Base()
        self.assertTrue(isinstance(b, Base))

    def test_istypeof(self):
        b = Base(40)
        self.assertEqual(type(b), Base)

    def test_has_attr(self):
        b = Base(10)
        self.assertTrue(hasattr(b, "id"))





if __name__ == "__main__":
    unittest.main()
