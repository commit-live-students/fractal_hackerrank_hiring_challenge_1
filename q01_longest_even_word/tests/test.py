import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from inspect import getfullargspec
from unittest import TestCase
from ..build import q01_longest_even_word


data1 = "One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading."
data2 = "photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading."
data3 = " testing very9 important"


class TestRead_textfile(TestCase):

    def test_args(self):
        arg = getfullargspec(q01_longest_even_word).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_even_strings(self):
        self.assertEqual(q01_longest_even_word(data1),'unfamiliar',"The Expected return String does not match with the return String")

    def test_even_strings_1(self):
        self.assertEqual(q01_longest_even_word(data2),'scanning',"The Expected return String does not match with the return String")

    def test_even_strings_2(self):
        self.assertEqual(q01_longest_even_word(data3),0,"The Expected return String does not match with the return String")
