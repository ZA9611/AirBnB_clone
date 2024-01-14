#!/usr/bin/python3
"""The __init__ special method for the directory of models."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
