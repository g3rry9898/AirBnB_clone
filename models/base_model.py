#!/usr/bin/python3

import uuid
from datetime import datetime
class BaseModel:
    def __init__(self):
        """initialize base model"""

        self.id = str(uuid.uuid4())
        """ generate unique id in string format"""

        self.created _at = datetime.now()
        self.updated_at = self.created_at

        """" date stamp created"""

    def save(self):

         self.updated_at = datetime.now()

        """save the time updated"""
    def to_dict(self):

        obj_dict = { '__class__': self.__class__.__name__,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

         return obj_dict
    def __str__(self):
         return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
