#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
	"""User class that's inherited from BaseModel."""
	email = ""
	password = ""
	frist_name = ""
	last_name = ""
