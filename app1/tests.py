"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from mylist import models


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

#    def test_models(self):
#        data = {"name": "battas", "date":"2222-11-11"}
#        models.Schedule.objects.create(**data)  
#        scs = models.Schedule.objects.all()
#        print scs
        
