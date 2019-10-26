import pytest
import os

from lib.kata_generator import KataGenerator
from lib.kata_generator_logger import KataGeneratorLogger

def test_kata_main_directory_existence():
    logger = KataGeneratorLogger()
    KataGenerator("test_kata", logger, ["param1"]).call()
    assert(os.path.isdir("./katas/test_kata")) == True

def test_kata_module_file_existence():
    logger = KataGeneratorLogger()
    KataGenerator("test_kata", logger, ["param1"]).call()
    assert(os.path.isfile("./katas/test_kata/__init__.py")) == True
    
def test_kata_readme_file_existence():
    logger = KataGeneratorLogger()
    KataGenerator("test_kata", logger, ["param1"]).call()
    assert(os.path.isfile("./katas/test_kata/README.md")) == True
    
def test_kata_test_definition_file_existence():
    logger = KataGeneratorLogger()
    KataGenerator("test_kata", logger, ["param1"]).call()
    assert(os.path.isfile("./tests/katas/test_test_kata.py")) == True