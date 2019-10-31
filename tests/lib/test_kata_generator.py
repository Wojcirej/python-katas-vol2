import unittest
import os
import shutil

from lib.kata_generator import KataGenerator
from lib.kata_generator_logger import KataGeneratorLogger
from lib.kata_generator_templater import KataGeneratorTemplater

class TestKataGenerator(unittest.TestCase):
  
    def setUp(self):
        self.logger = KataGeneratorLogger()
        self.templater = KataGeneratorTemplater("test_kata")
        KataGenerator("test_kata", self.logger, self.templater, ["param1"]).call()
        
    def tearDown(self):
        if os.path.isdir("./katas/test_kata") == True:
            shutil.rmtree("./katas/test_kata")
        if os.path.isfile("./tests/katas/test_test_kata.py") == True:
            os.remove("./tests/katas/test_test_kata.py")

    def test_kata_main_directory_existence(self):
        "creates directory for kata in katas directory"
        assert(os.path.isdir("./katas/test_kata")) == True

    def test_kata_module_file_existence(self):
        "creates module declaration file in kata directory"
        assert(os.path.isfile("./katas/test_kata/__init__.py")) == True
    
    def test_kata_readme_file_existence(self):
        "creates README file in kata directory"
        assert(os.path.isfile("./katas/test_kata/README.md")) == True
    
    def test_kata_test_definition_file_existence(self):
        "creates file for unit tests in tests/katas/ directory"
        assert(os.path.isfile("./tests/katas/test_test_kata.py")) == True