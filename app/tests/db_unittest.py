import unittest
from flask_testing import TestCase
from app import create_app, DB as db
import os

class DataBaseUnittest(TestCase):

    def create_app(self):
        """Return app context."""
        return create_app("test")

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        """Drop dataBase"""
        db.session.remove()
        db.drop_all()