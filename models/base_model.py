#!/usr/bin/python3
"""This script is the base model"""

import uuid
from datetime import datetime
from models import file_storage


class BaseModel:

    """All classes inherits from this class"""
    def __init__(self):

        """attributes to be used by the instances"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now
        self.updated_at = datetime.now
    def __str__(self):

        """returns a string representation"""

        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):

        """update the public instance"""

        self.updated_at = datetime.now()
    def to_dict(self):
        """returns dictionary containing all keys and value pair"""
        json_dict = self.__dict__()
        json_dict["__class__"] = self.__class__.__name__
        json_dict["created_at"] = json_dict["created_at"].isoformat()
        json_dict["updated_at"] = json_dict["updated_at"].isoformat()
        return json_dict
