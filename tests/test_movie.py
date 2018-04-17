import unittest

from models import Movie

class MovieTest(unittest.TestCase):
    '''
    Test class test the behaviour of our Model
    '''

    def setUp(self):
        '''
        Setup method before every test
        '''

        self.new_movie=Movie(12,"Python Must Be Crazy",'A crazy Python series','khsjha27hbs',8.5,123)


    def test_instance(self):
        '''
        Testing the Instance of the variable created
        '''

        self.assertTrue(isinstance(self.new_movie,Movie))
