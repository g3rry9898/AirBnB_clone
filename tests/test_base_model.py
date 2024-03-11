#!/usr/bin/python3
import unittest
from base_model import BaseModel

class TestBaseModel(unittest.testcase):

    def setUp(self):
        self.base_model =  BaseModel

    def test_id_is_unique(self):
        example_base_model = BaseModel()
        
        self.assertNotEqual(self.base_model.id, example_base_model.id)
       
    def test_created_at_is_set(self):

        self.assertIsNotNone(self.base_model.created_at)

    def test_update_at_is_same_as_created_at(self):

        self.assertEqual(self.base_model.created_at, self.base_model.updated_at)

    def test_save_updates_updated_at(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)
    
